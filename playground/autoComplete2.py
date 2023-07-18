
import pickle
# autocompatte index 
with open('app\search_engine\data\\Trie', 'rb') as fl:
    trie = pickle.load(fl)
    print('loaded the trie tree structure')



def getSuggestions(query):
    return ''
    

def saveQuery(query):
    return ''
    
def saveAutoCompleteIndex():
    with open('app\search_engine\data\\autocomlist', 'wb') as fout:
        pickle.dump(trie, fout)
        print('autocomplete list saved')

    