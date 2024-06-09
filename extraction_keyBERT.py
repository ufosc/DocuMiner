from keybert import KeyBERT
from sklearn.feature_extraction.text import CountVectorizer
import openpyxl
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

kw_model = KeyBERT()


# Currently only setup to work for single file document

# creates Excel sheet of keywords similar to user's keywords
def create_excel_file_similarity(text_doc):
    print()
    create_file = input(
        "     Would you like to create an excel file for similar keywords to a predefined list? (Y/N): ")
    create_file = create_file.upper()

    if create_file == "Y":

        # extract 10 keywords
        data = kw_model.extract_keywords(text_doc, top_n=10)

        # Predefined list of keywords
        existing_keywords_str = input("     Please enter list of keywords to compare "
                                      "against? (separate keywords by commas): ")
        existing_keywords = [token.strip() for token in existing_keywords_str.split(',')]

        # Find similar keywords
        similar_keywords = find_similar_keywords(data, existing_keywords)

        workbook = openpyxl.Workbook()
        sheet = workbook.active
        sheet.append(["Keyword", "Similar to", "Similarity score"])
        for row in similar_keywords:
            sheet.append(row)

        filename = input("     Name your excel file: ")
        workbook.save("../excel_files/" + filename + ".xlsx")

        print("     Excel file created successfully!\n")


# creates an Excel sheet with table of keyword data
def create_excel_file(text_doc):
    print()
    create_file = input("     Would you like to create an excel file from your keywords? (Y/N): ")
    create_file = create_file.upper()

    if create_file == "Y":
        customizations = input("     Would you like to customize your keywords? (Y/N): ")
        customizations = customizations.upper()

        if customizations == "Y":
            # setup custom settings
            data = get_custom_keywords(text_doc)
        else:
            # default settings
            data = get_keywords(text_doc)

        workbook = openpyxl.Workbook()
        sheet = workbook.active
        sheet.append(["Keyword", "Cosine Similarity Value"])
        for row in data:
            sheet.append(row)

        filename = input("     Name your excel file: ")
        workbook.save("../excel_files/" + filename + ".xlsx")

        print("     Excel file created successfully!\n")


# gets keywords using default settings
def get_keywords(doc):
    keywords = kw_model.extract_keywords(doc)
    return keywords


# considers number of keywords/phrases, length of keywords/phrases,
# stop words, and diversity
def get_custom_keywords(doc):
    # number of keywords/phrases
    num = get_num_keys()

    # length of keywords
    phrase_range = get_range_values()
    my_vectorizer = CountVectorizer(ngram_range=phrase_range)

    # english stop words
    include_stops = input("     Do you want to exclude stop words from keyphrases? (Y/N): ")
    include_stops = include_stops.upper()
    if include_stops == "Y":
        my_vectorizer = CountVectorizer(ngram_range=phrase_range, stop_words="english")

    # diversity settings
    include_diversity = input("     Do you want to consider the diversity of your keyphrases? (Y/N): ")
    include_diversity = include_diversity.upper()
    if include_diversity == "Y":
        diversity_value = get_diversity_value()
        keywords = kw_model.extract_keywords(doc, vectorizer=my_vectorizer, use_mmr=True, diversity=diversity_value,
                                             top_n=num)
    else:
        keywords = kw_model.extract_keywords(doc, vectorizer=my_vectorizer, top_n=num)

    return keywords


# Helper Functions


# gets number of keywords from user
def get_num_keys():
    num_keys = 0
    not_valid = True
    while not_valid:
        try:
            num_keys = input("     How many keywords/phrases do you want returned?"
                             " (value must be an integer greater than 0): ")
            num_keys = int(num_keys)
            if num_keys >= 1:
                not_valid = False
            else:
                print("     Integer must be greater than 0")
        except ValueError:
            print("     Please enter an integer...")
    return num_keys


# gets keyphrase word range from user
def get_range_values():
    range_min = 1
    range_max = 1
    custom_length = input("     Do you want to customize length of keyphrases? (Y/N): ")
    custom_length = custom_length.upper()
    if custom_length == "Y":
        valid_num = True
        while valid_num:
            try:
                value = input("     Enter minimum length of keyphrase: ")
                range_min = int(value)
                valid_num = False
            except ValueError:
                print("     Please enter an integer...")

        valid_num = True
        while valid_num:
            try:
                value = input("     Enter maximum length of keyphrase: ")
                range_max = int(value)
                valid_num = False
            except ValueError:
                print("     Please enter an integer...")
    return range_min, range_max


# gets diversity value from user
def get_diversity_value():
    value = 0
    is_not_float = True
    while is_not_float:
        try:
            value = input("     Enter diversity value (between 0 and 1): ")
            value = float(value)
            while value < 0 or value > 1:
                print("     Please enter a number between 0 and 1...")
                value = input("     Enter diversity value (between 0 and 1): ")
                value = float(value)
            is_not_float = False

        except ValueError:
            print("     Please enter a number...")
    return value


# computes similarity between keywords
def find_similar_keywords(extracted_keywords, predefined_keywords):
    model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

    # Extract keyword strings from tuples
    extracted_keyword_strings = [kw[0] for kw in extracted_keywords]

    # Generate embeddings for the keywords
    extracted_embeddings = model.encode(extracted_keyword_strings)
    predefined_embeddings = model.encode(predefined_keywords)

    # Compute cosine similarity
    similarities = cosine_similarity(extracted_embeddings, predefined_embeddings)

    # Find the most similar predefined keyword for each extracted keyword
    similar_keywords = []
    for i, sim_scores in enumerate(similarities):
        max_sim_idx = np.argmax(sim_scores)
        similar_keywords.append(
            (extracted_keyword_strings[i], predefined_keywords[max_sim_idx], sim_scores[max_sim_idx]))

    return similar_keywords
