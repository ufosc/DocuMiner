from readability import Readability

def rank(fileNames, documents):

    #FUTURE ADDITIONS: More scoring metrics, more filter options

    for file in fileNames:
        rank_obj = Readability(documents[file]["text"])

        # Flesh Kincaid Ranking. More info: https://en.wikipedia.org/wiki/Flesch%E2%80%93Kincaid_readability_tests
        # Lower Score = Higher Reading Level
        #   --Ex: Score 100-90 -> 5th Grade, Score 30-10 -> College Graduate 
        
        documents[file]["score"] = rank_obj.flesch_kincaid().score
    
    documents_ordered = {key: val for key, val in sorted(documents.items(), key=lambda item: item[1]["score"], reverse=True)}
    
    option = int(input(
        "Ranking Options:\n"+
        "1. Lowest Score (Higher Reading Level) -> Highest Score (Lower Reading Level)\n"+ 
        "2. Highest Score (Lower Reading Level) -> Lowest Score (Higher Reading Level)\n"+
        "Enter Option Number: "))

    reverse = False
    if option == 1:
        reverse = False
    if option == 2:
        reverse = True
        
    documents_ordered = {key: val for key, val in sorted(documents.items(), key=lambda item: item[1]["score"], reverse=reverse)}

    return list(documents_ordered.keys())
    