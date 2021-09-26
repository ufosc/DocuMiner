import spacy
from nltk.corpus import stopwords

def tagSpacy(text): #tag the english text
    nlp = spacy.load("en_core_web_sm")
    return nlp(text)


def extractNamedEntitySpacy(text,entity,alreadyNLP = True): #search for certain entity and return the occurences
    if not alreadyNLP: #fpr entity in spacy entity labels for example "PERSON"
        nlp = spacy.load("en_core_web_sm")
        doc = nlp(text)
    else:
        doc = text

    entityList = [(token.text, token.label_) for token in doc.ents]
    return [token for token in entityList if token[1] in entity]

#extractNamedEntitySpacy(text,["GPE","PERSON"],alreadyNLP = False)


def posListSpacy(text,removeStop = True,removePunc = True, alreadyNLP = True,filterTag =""): #returns pos tag list for spacy text
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
