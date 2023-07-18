from numpy import empty
import pandas as pd 
l = [1, 3, 9]
docs = ["a", "b", "c"]


docMapper = dict(zip(range(0, len(docs)), docs))
df = pd.DataFrame({'docs':   docMapper.keys() })



print(df.docs.values)

dx = {}
dx['3'] = 3
dx['5'] = 3
print(dx.get('5', 0))
print((dx.get('35')))

docsIds = []
if not docsIds:
    print('hi')