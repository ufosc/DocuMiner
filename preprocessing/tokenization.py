from requests.models import MissingSchema
from nltk.tokenize import sent_tokenize, word_tokenize
import nltk
import os, sys
from bs4 import BeautifulSoup
import requests
import extraction_keyBERT


def main():
    fileNames = []
    words = []
    sentences = []
    path = os.getcwd()
    
    # UNCOMMENT FOR FUNCTIONS

    # words, sentences = URL(words, sentences)

    # singleFile(fileNames)
    # words, sentences, text = tokenizeFiles(fileNames, path)
    # extraction_keyBERT.create_excel_file(text)

    fileNames = multipleFiles(fileNames)
    words, sentences, text = tokenizeFiles(fileNames, path)
    extraction_keyBERT.create_excel_file(text)
    extraction_keyBERT.create_excel_file_similarity(text)

    # fileNames, path = directory(fileNames)
    # words, sentences, text = tokenizeFiles(fileNames, path)
    # extraction_keyBERT.create_excel_file(text)

    print('Words: ', words, '\nSentences: ', sentences)


# Scrapes and Tokenizes txt from URL
def URL(words, sentences):
    # Scrapes data from URL
    url = input("Enter URL: ")
    try:
        html = requests.get(url)
    except MissingSchema: 
        print("Invalid URL, no schema supplied. Perhaps you meant http://{0}?".format(url))
        sys.exit()

    raw = BeautifulSoup(html.text, 'html.parser').get_text()

    searchWord = input(
        "Enter search keyword (ENTER to parse entire html page): ")
    wordTokens = word_tokenize(raw)
    words = word_tokenize(raw)
    sentences = sent_tokenize(raw)
    # Turns text into nltk object, concordance searches and returns keyword w/text around it in array
    if(searchWord != ""):
        wordObj = nltk.Text(wordTokens)
        # Prints out concordance to terminal (VISUAL), does not save to array
        wordObj.concordance(searchWord)
        # Saves concordance to array wrapped in an nltk object type
        words = wordObj.concordance_list(searchWord, width=150)

    return words, sentences


# Pulls filenames from Directory
def directory(fileNames):
    path = os.getcwd()
    usrInput = input("Enter full path (ENTER for working directory): ")
    if usrInput != "":
        path = usrInput
    if(os.path.exists(path)):
        dirFiles = [x for x in os.listdir(path) if x.endswith(".txt")]
        for file in dirFiles: fileNames.append(file)
        return fileNames, path
    else:
        print("ERROR: directory not found")
        return fileNames, path

# Generates list of Single or Multiple files


def singleFile(fileNames):
    usrInput = input("Enter file name: ")
    fileNames.append(usrInput)
    return fileNames


def multipleFiles(fileNames):
    usrInput = input("Enter file name: ")
    fileNames = [usrInput]
    while usrInput != "":
        fileNames.append(usrInput)
        usrInput = input("Enter file name (ENTER to terminate): ")
    return fileNames


# Tokenizes txt files, run after multipleFiles() or singleFile()
def tokenizeFiles(fileNames, path):
    words = []
    sentences = []
    text = ""
    try:
        for fileName in fileNames:
            with open(os.path.join(path, fileName), encoding='utf-8') as file:
                text = text + " " + file.read()
                words.append(word_tokenize(text))
                sentences.append(sent_tokenize(text))

    except IOError as e:
        print("I/O error({0}): {1}".format(e.errno, e.strerror))
    except OSError:
        print(f"OS error trying to open {fileName}")

    return words, sentences, text


main()
