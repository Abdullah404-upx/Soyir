q = ['hello', 'there', 'out']

wordIndex = {"hello": [1, [1, 3 ,4 ]]}

def getDocsIds_of_query(query):
    a = set()
    
    for q in query: 
        if wordIndex.get(q) is not None:
            #print(wordIndex[q])
            a.update((wordIndex[q][1]))
            print("hhahahahha")
        else:
            print("the word (", q , ") is not in the index")
            
    return dict.fromkeys(list(a), 0)

def all_query_terms_existInIndex(query):
    for q in query:
        if wordIndex.get(q, None) == None: 
            return "yes"

print(all_query_terms_existInIndex(q))
