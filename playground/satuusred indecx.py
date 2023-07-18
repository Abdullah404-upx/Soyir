#https://web.stanford.edu/class/cs276/handouts/lecture12-bm25etc.pdf


from Preprocessing import cleanText
import math
import time  
import json
import pandas as pd 


df = pd.read_csv('app\search_engine\data\movies_data.csv', usecols= ['_id', 'overview', 'original_title', 'release_date'])
#print(str(df["overview"][0]))
#print(str(df['original_title'][1])+ ". " + str(df['overview'][1]))

wordIndex = {}
docIndex = {}

N = len(df)


titleWeight = 4
dateWeight = 3
paragraphWeight = 2

avgTitle = None
avgParagraph = None 
b = .75 




def cleanTheDataframe():
    for i in range(N): 
        df['original_title'][i] = ' '.join(cleanText(str(df['original_title'][i])))
        df['overview'][i]= ' '.join(cleanText(str(df['overview'][i])))
        df['release_date'][i] = ' '.join(cleanText(str(df['release_date'][i])))

    
    

def calculateIDF():
    for word in wordIndex.keys():
        nq = len(wordIndex[word][1])
        wordIndex[word][0] = math.log((N - nq + 0.5 / nq + .5) + 1 )
        


# build vocab and calcuaiton tf 

def buildVocab(doc): 

    docTextArray = doc["text"]
    a= set(doc["text"].split(' '))


    document = (docTextArray).split('hhh')
 #   print(document)
  #  print(document)
    for word in a:
        if word != 'hhh':
            bTitle = ((1-.75) + .75 * len(document[0]) / avgTitle)
            bParagraph = ((1-.75) + .75 * len(document[1]) / avgParagraph)
            #bParagraph = 1
            try:
                
                wordIndex[word][1][doc["id"]] =  ((titleWeight * document[0].count(word)) / bTitle ) + ((paragraphWeight * document[1].count(word)) / bParagraph) + (dateWeight * document[2].count(word))
            except:
                wordIndex[word] = [0, {}]
                wordIndex[word][1][doc["id"]] =  ((titleWeight * document[0].count(word)) / bTitle ) + ((paragraphWeight * document[1].count(word)) / bParagraph) + (dateWeight * document[2].count(word))




def saveIndex():
    with open('app\search_engine\data\satuareted.json', 'w') as outfile:
        json.dump(wordIndex, outfile)
        print(wordIndex.keys())
  #  with open('app\search_engine\data\docindexFF.json', 'w') as outfile:
  #      json.dump(docIndex, outfile)
    print(len(wordIndex), 'terms and ', len(df), ' docs have been indexed and saved.')


###############################################


def buildInvertedIndex():
    s = time.time()


    cleanTheDataframe()
    
    frameTiles = df['original_title'].to_list()
    frameParagraps = df['overview'].to_list()

    titles = [len(title) for title in frameTiles]
    paragraphs = [len(par) for par in frameParagraps]

    global avgTitle, avgParagraph
    avgTitle = sum(titles) / len(titles)
    avgParagraph = sum(paragraphs) / len(paragraphs)

    
    
    doc = {}

    for i in range(N): 
        doc["id"] = i 
        #doc["text"] = cleanText(str(df['original_title'][i])+ ". " + str(df['overview'][i]) + ". " + str(df['release_date'][i])[0:4])
        doc["text"] = str(df['original_title'][i])+ " hhh " + str(df['overview'][i]) + " hhh " + str(df['release_date'][i])[0:4]
        #print(doc['text'], 'is the text')
     #   docIndex[doc["id"]] = len(doc["text"]) -1  # the hhh
        buildVocab(doc)    
    
    
    
    calculateIDF()

    saveIndex()    
    print("indexing process took ", ((time.time() - s)), 'seconds')


    
buildInvertedIndex()
 

#print(wordIndex)
###############################################################

			

