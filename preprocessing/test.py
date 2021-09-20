from nltk.tokenize import sent_tokenize, word_tokenize
import nltk
import os
from bs4 import BeautifulSoup
import requests
nltk.download('punkt')


def main():
    fileNames = []
    words = []
    sentences = []

    # UNCOMMENT FOR FUNCTIONS

    words, sentences = URL(words, sentences)

    # singleFile(fileNames)
    # tokenizeFiles(fileNames)

    # multipleFiles(fileNames)
    # tokenizeFiles(fileNames)

    # fileNames = directory(fileNames)
    # words, sentences = tokenizeFiles(fileNames)

    print("words: ", words, "\nsentences: ", sentences)


# Tokenizes from URL
def URL(words, sentences):
    url = input("Enter URL: ")
    try:
        html = requests.get(url)
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)

    raw = BeautifulSoup(html.text, 'html.parser').get_text()

    searchWord = input(
        "Enter search keyword (ENTER to parse entire html page): ")
    wordTokens = word_tokenize(raw)
    sentences = sent_tokenize(raw)
    # Turns text into nltk object, concordance searches and returns keyword w/text around it in array
    if(searchWord != ""):
        wordObj = nltk.Text(wordTokens)
        words = wordObj.concordance_list(searchWord, width=150)
    return words, sentences


# Pulls filenames from Directory
def directory(fileNames):
    path = os.getcwd()
    usrInput = input("Enter full path (ENTER for working directory): ")
    if usrInput != "":
        path = usrInput
    dirFiles = [x for x in os.listdir(path) if x.endswith(".txt")]
    for file in dirFiles:
        fileNames.append(file)
    return fileNames

# Single and Multiple files


def singleFile(fileNames):
    usrInput = input("Enter file name: ")
    fileNames = [usrInput]
    return fileNames


def multipleFiles(fileNames):
    usrInput = input("Enter file name: ")
    fileNames = [usrInput]
    while usrInput != "":
        fileNames.append(usrInput)
        usrInput = input("Enter file name (ENTER to terminate): ")
    return fileNames


# Tokenizes txt files
def tokenizeFiles(fileNames):
    words = []
    sentences = []
    try:
        for fileName in fileNames:
            with open(fileName, encoding='utf-8') as file:
                text = file.read()
                words.append(word_tokenize(text))
                sentences.append(sent_tokenize(text))
                print('Words: ', words, '\nSentences: ', sentences)

    except IOError as e:
        print("I/O error({0}): {1}".format(e.errno, e.strerror))
    except OSError:
        print(f"OS error trying to open {fileName}")

    return words, sentences


main()
