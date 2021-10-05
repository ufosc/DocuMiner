from requests.models import MissingSchema
from nltk.tokenize import sent_tokenize, word_tokenize
import nltk
import os, sys
from bs4 import BeautifulSoup
import requests
import pdfplumber
import docx2txt
# nltk.download('punkt')


def URL():
    """
    Asks user for URL to scrape raw text from

    Returns:
        raw text in string form 
    """
    
    url = input("Enter URL: ")
    try:
        html = requests.get(url)
    except MissingSchema: 
        print("Invalid URL, no schema supplied. Perhaps you meant http://{0}?".format(url))
        sys.exit()

    raw = BeautifulSoup(html.text, 'html.parser').get_text()
    return raw


def directory(fileNames):
    """
    Pulls all .txt, .pdf, and .docx filenames from directory

    Parameters: fileNames - empty array to append to

    Returns: 
        fileNames - all fileNames from directory
        path - string containing directory path
    """
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



def singleFile(fileNames):
    """
    Asks user for single file from specific path

    Parameters: fileNames - empty array to append to

    Returns:
        fileNames - single fileName from specific directory
        path - string containing directory path containing single file
    """
    path = os.getcwd
    pathInput = input("Enter directory with file (ENTER for working directory): ")
    usrInput = input("Enter file name: ")
    fileNames.append(usrInput)
    if pathInput != "": path = pathInput
    return fileNames, path


def multipleFiles(fileNames):
    """
    Asks user for multiple files from specific path

    Parameters: fileNames - empty array to append to

    Returns:
        fileNames - array of fileNames from specific directory
        path - string containing directory path containing multiple files
    """
    path = os.getcwd
    pathInput = input("Enter directory with files (ENTER for working directory): ")
    usrInput = input("Enter file name: ")
    fileNames = [usrInput]
    while usrInput != "":
        usrInput = input("Enter file name (ENTER to terminate): ")
        if usrInput != "":
            fileNames.append(usrInput)
    if pathInput != "": path = pathInput
    return fileNames, path


def getRawText(fileNames, path, documents):
    """
    Generates raw text array from given filenames and path

    Parameters: 
        fileNames - array of fileNames to iterate through
        path - string containing directory path used to find files
        documents - 

    Returns:
        textArray - string array containing all raw text from each file in fileName
    """
    textArray = []
    try:
        for fileName in fileNames:
            text = ""
            if fileName.endswith(".txt"):
                with open(os.path.join(path, fileName), encoding='utf-8') as file:
                    text = file.read()
                    documents[fileName] = {}
                    documents[fileName]["text"] = text.replace("\n", "") #remove \n from text 
                    documents[fileName]["score"] = 0
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

