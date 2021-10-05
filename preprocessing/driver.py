import tokenization, spacy_entity_preprocessing, pos_tag, ranker, question_answer
import os
import nltk, spacy
import en_core_web_sm
from nltk.corpus import stopwords
# nltk.download('averaged_perceptron_tagger')


def main():
    path = ''
    fileNames = []
    text = []
    documents = {}
    
    # UNCOMMENT FOR FUNCTIONS

    # text.append(tokenization.URL())

    # fileNames, path = tokenization.singleFile(fileNames)
    # text = tokenization.getRawText(fileNames, path)

    fileNames, path = tokenization.multipleFiles(fileNames)
    text = tokenization.getRawText(fileNames, path, documents)

    #Question and answering
    # results = question_answer.questionAnswer(fileNames, documents)
    # print("\nInfo: " + str(results))
    # print("\nAnswer: " + results['answer'])
    

    #Ranker 
    #documents_ordered = ranker.rank(fileNames, documents)
    #print(documents_ordered)
    
    # fileNames, path = tokenization.directory(fileNames)
    # text = tokenization.getRawText(fileNames, path)

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