import pickle
from fast_autocomplete import autocomplete_factory
from fast_autocomplete import AutoComplete
with open('mypickle.pickle', 'rb') as fl:
    words = pickle.load(fl)
    print('loaded')



autocomplete = AutoComplete(words=words)
print(autocomplete.words)