import pandas as pd 
import json 
# https://image.tmdb.org/t/p/w500//vzmL6fP7aPKNKPRTFnZmiUfciyV.jpg

df = pd.read_csv('app\search_engine\data\dataset.csv',  usecols= ['original_title'])

titles = df['original_title'].to_list()

final_dict = {}
for title in titles:
    final_dict[title.lower()] = [{}, title, 1]

with open('dict.json', 'w') as out:
    json.dump(final_dict, out)
    print('saved')

#print(df.head)


# alpha = range(0, 10000)
# alpha = list(map(str,alpha))
