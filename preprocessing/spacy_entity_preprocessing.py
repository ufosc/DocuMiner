import spacy
from nltk.corpus import stopwords

def tagSpacy(text): #tag the english text
    """
    Make text into a Spacy NLP object
    Add a multiline string

    Prameters:
        text (str) - multiline string, paragraph or article

    Returns:
        Spacy nlp object
    """
    nlp = spacy.load("en_core_web_sm")
    return nlp(text)


def extractNamedEntitySpacy(text,entity,alreadyNLP = True): #search for certain entity and return the occurences
    """
    Mine specefic key words from a text or nlp object

    Parameters:
        text (str/nlp) - multiline string, paragraph or article
        entities (list) - list of the spacy named entities want to mine for ["GPE","PERSON"] for example
        alreadyNLP (bool) - if orginally string converts to NLP, default is True

    Returns:
        Multilevel list - list of objects and its entity together

    """

    if not alreadyNLP: #fpr entity in spacy entity labels for example "PERSON"
        nlp = spacy.load("en_core_web_sm")
        doc = nlp(text)
    else:
        doc = text

    entityList = [(token.text, token.label_) for token in doc.ents]
    return [token for token in entityList if token[1] in entity]

#extractNamedEntitySpacy(text,["GPE","PERSON"],alreadyNLP = False)


def posListSpacy(text,removeStop = True,removePunc = True, alreadyNLP = True,filterTag =""): #returns pos tag list for spacy text

    """
    Return a part of speech list for spacy, each word assigned a part of speech

    Parameters:
        text (str/nlp) - multiline string, paragraph or article
        removeStop (bool) - remove english stopwords, default True
        removePunc (bool) - remove punctuation, default True
        filterTag (str) - filter to Spacy parts of speech, nouns, verbs, etc, default does not filter

    Returns:
        Multilevel list with each word assigned a part of speech
    """

    if not alreadyNLP: #note useless step since with spacy can already recognize pos tag by .tag_
        nlp = spacy.load("en_core_web_sm")
        pos_list = nlp(text)
    else:
        pos_list = text

    pos_list = [(X.text, X.tag_) for X in pos_list]

    if removeStop:
        pos_list = [word for word in pos_list if not word[0].lower() in set(stopwords.words('english'))]

    if removePunc:
        pos_list = [word for word in pos_list if word[0].isalnum()]

    if len(filterTag) != 0:
        pos_list = [word for word in pos_list if word[1] == filterTag]

    return pos_list
