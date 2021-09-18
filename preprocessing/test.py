from nltk.util import filestring
from nltk.tokenize import sent_tokenize, word_tokenize
import nltk
import os
# nltk.download('punkt')

usrInput = input("Enter file name: ")
fileNames = [usrInput]


while usrInput != "":
    fileNames.append(usrInput)
    usrInput = input("Enter file name (ENTER to terminate): ")


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
