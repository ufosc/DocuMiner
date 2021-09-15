import nltk
# nltk.download('punkt')
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.util import filestring

fileName = input("Enter File Name: ")
try: 
    with open(fileName, encoding='utf-8') as file:
        text = file.read()
        words = word_tokenize(text)
        sentences = sent_tokenize(text)
        print('Words: ', words, '\nSentences: ', sentences)

except IOError as e:
    print("I/O error({0}): {1}".format(e.errno, e.strerror))
except OSError:
    print(f"OS error trying to open {fileName}")

