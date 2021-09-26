from requests.models import MissingSchema
from nltk.tokenize import sent_tokenize, word_tokenize
import nltk
import os, sys
from bs4 import BeautifulSoup
import requests
import pdfplumber
import docx2txt

# Scrapes and Tokenizes txt from URL
def URL():
    # Scrapes data from URL
    url = input("Enter URL: ")
    try:
        html = requests.get(url)
    except MissingSchema: 
        print("Invalid URL, no schema supplied. Perhaps you meant http://{0}?".format(url))
        sys.exit()

    raw = BeautifulSoup(html.text, 'html.parser').get_text()
    print(raw)

    return raw


# Pulls filenames from Directory
def directory(fileNames):
    path = os.getcwd()
    usrInput = input("Enter full path (ENTER for working directory): ")
    if usrInput != "":
        path = usrInput
    if(os.path.exists(path)):
        dirFiles = [x for x in os.listdir(path) if x.endswith((".txt", ".pdf", ".docx"))]
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
    textArray = []
    try:
        for fileName in fileNames:
            text = ""
            if fileName.endswith(".txt"):
                with open(os.path.join(path, fileName), encoding='utf-8') as file:
                    text = file.read()
                    textArray.append(text)
            
            elif fileName.endswith(".pdf"):
                with pdfplumber.open(os.path.join(path, fileName)) as file:
                    pages = file.pages
                    for page in pages:
                        text += page.extract_text()
                    textArray.append(text)
                    
            
            elif fileName.endswith(".docx"):
                text = docx2txt.process(os.path.join(path, fileName))
                textArray.append(text)

    except IOError as e:
        print("I/O error({0}): {1}".format(e.errno, e.strerror))
    except OSError:
        print(f"OS error trying to open {fileName}")

    return textArray

