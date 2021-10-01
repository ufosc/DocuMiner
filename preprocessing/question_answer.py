from transformers import pipeline
from tokenization import singleFile
import os


def questionAnswer(fileNames, documents):
    #Basic pipeline used with default model, may change later
    
    context = None

    while(context == None):

        if(len(fileNames) == 1):
            #If only one file, auto choose it
            context = fileNames[0]

        else:
            option = int(input("Choose the file (0 for first, 1 for second...): "))

            try:
                file_name = fileNames[option]
                context = documents[file_name]["text"]

            except IndexError:
                print("Option entered greater than number of files inputted")

    nlp = pipeline("question-answering")

    question = input("Enter a question about the text: ")

    results = nlp(question=question, context=context)

    return results

