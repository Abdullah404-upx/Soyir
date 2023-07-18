import pandas as pd 
import json 
import pickle
from fast_autocomplete import autocomplete_factory


df = pd.read_csv('app\search_engine\data\dataset.csv',  usecols= ['original_title'])

titles = df['original_title'].to_list()

final_dict = {}
for title in titles:
    final_dict[title.lower()] = [{}, title, 1]

with open('dict.json', 'w') as out:
    json.dump(final_dict, out)
    print('saved')




content_files = {
    'words': {
        'filepath': 'dict.json',
        'compress': True  # means compress the graph data in memory
    }
}

autocomplete = autocomplete_factory(content_files=content_files)

print(autocomplete.search(word="toy s"))
print(autocomplete.words['toy story'].display)
#print(autocomplete.words)
print(autocomplete.search(word="toy"))

print(type(autocomplete))
print(autocomplete.words['toy story'])
with open('autocomlist', 'wb') as f:
    pickle.dump(autocomplete.words, f)
    print('saved auto copmalte index')
