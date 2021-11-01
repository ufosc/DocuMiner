import nltk
from nltk.corpus import stopwords

def TagText(text, splitByWord = True,removeStop = True, removePunc = True):

    """
    Tags the text using the NLTK library, each word assigned a part of speech

    Parameters:
        text (str) - multiline string, paragraph or article
        splitByWord - splits the text string by word
        removeStop - remove english stop words, default true
        removePunc - remove punctuation, default true

    Return:
        Multilevel list with each word assigned a part of speech
    """
    if splitByWord:
        tokens = nltk.word_tokenize(text)
    else:
        tokens = text

    if removeStop:
        stop_words = set(stopwords.words('english')) #removes all repeats
        tokens = [word for word in tokens if not word.lower() in stop_words] #removes stop words with list comprehension

    if removePunc:
        tokens = [word for word in tokens if word.isalnum()] #removes all things are not only alphanumeric

    return nltk.pos_tag(tokens)

def filterByTag(tagArray,pos): #function filters by pos tags
    return [tagSet for tagSet in tagArray if tagSet[1] == pos]
