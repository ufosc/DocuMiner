import nltk
import os
from bs4 import BeautifulSoup
import requests
nltk.download('punkt')
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.util import filestring

def main():
    fileNames = []
    words = []
    sentences = []
    
    # UNCOMMENT FOR FUNCTIONS

    URL(words, sentences)

    # singleFile(fileNames)
    # tokenizeFiles(fileNames)

    # multipleFiles(fileNames)
    # tokenizeFiles(filNames)

    # directory(fileNames)
    # tokenizeFiles(fileNames)



# Tokenizes from URL
def URL(words, sentences):
    url = input("Enter URL: ")
    html = requests.get(url)
    raw = BeautifulSoup(html.text, 'html.parser').get_text()
    print(raw)
    wordTokens = word_tokenize(raw)
    sentences = sent_tokenize(raw)
    # Turns text into nltk object, concordance searches and returns search keyword
    # wordObj = nltk.Text(wordTokens)
    # words = wordObj.concordance("SEARCH_KEY_WORD")
    return words, sentences


# Pulls filenames from Directory
def directory(fileNames):
    path = os.getcwd()
    usrInput = input("Enter full path (ENTER for working directory): ")
    if usrInput != "": path = usrInput
    dirFiles = [x for x in os.listdir(path) if x.endswith(".txt")]
    for file in dirFiles: fileNames.append(file) 

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
    try: 
        for fileName in fileNames:
            with open(fileName, encoding='utf-8') as file:
                text = file.read()
                words = word_tokenize(text)
                sentences = sent_tokenize(text)
                print('Words: ', words, '\nSentences: ', sentences)

    except IOError as e:
        print("I/O error({0}): {1}".format(e.errno, e.strerror))
    except OSError:
        print(f"OS error trying to open {fileName}")

main()