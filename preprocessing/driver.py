import tokenization, spacy_entity_preprocessing, pos_tag
import os
import nltk, spacy
import en_core_web_sm
from nltk.corpus import stopwords
nltk.download('averaged_perceptron_tagger')


def main():
    path = os.getcwd()
    fileNames = []
    text = []
    
    # UNCOMMENT FOR FUNCTIONS

    # text.append(tokenization.URL())

    # fileNames = tokenization.singleFile(fileNames)
    # text = tokenization.tokenizeFiles(fileNames, path)

    fileNames = tokenization.multipleFiles(fileNames)
    text = tokenization.tokenizeFiles(fileNames, path)

    # fileNames, path = tokenization.directory(fileNames)
    # text = tokenization.tokenizeFiles(fileNames, path)

    #Prints Raw Text
    print("Raw Text: ", text)

    #POS Tagging for NLTK
    # for i in range(len(text)):
    #     text[i] = pos_tag.TagText(text[i])

    #POS Tagging for Spacy
    for i in range(len(text)):
        text[i] = spacy_entity_preprocessing.tagSpacy(text[i])

    #For spacy entity, prints chunks that meet "GPE" and "PERSON" criteria
    for file in text:
        print('Filtered Text: ', spacy_entity_preprocessing.extractNamedEntitySpacy(file,["GPE","PERSON"],alreadyNLP = True))
    
   


main()