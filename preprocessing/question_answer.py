from transformers import pipeline
from tokenization import singleFile
import os

def questionAnswer(fileNames, text):
    ''' Runs a question answering routine using terminal user input
        fileNames - list of file names
        text - text[i] is the text of the ith file in fileNames
    '''
    context = None
    print(fileNames)

    while(context == None):
        if(len(fileNames) == 1):
            #If only one file, auto choose it
            context = text[0]
        else:
            option = int(input("Choose the file (0 for first, 1 for second...): "))
            try:
                context = text[option]
            except IndexError:
                print("Option entered greater than number of files inputted")

    nlp = pipeline("question-answering")
    question = input("Enter a question about the text: ")
    results = nlp(question=question, context=context)
    return results
