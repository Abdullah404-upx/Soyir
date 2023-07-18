
 

from asyncio import threads
import threading
import requests
import concurrent.futures
from pymongo import MongoClient

def connectDB():
    mongoDriver = 'mongodb+srv://zzzzzzzzzzzzzz@cluster0.5axsa.mongodb.net/0000000000?retryWrites=true&w=majority'
    client = MongoClient(mongoDriver)
    return client


client = connectDB()
db = client['00000000']
mycollection = db['movies']



# LOL
def updatePoster(i):
  movie =  mycollection.find_one({'_id': str(i)})
  #print(movie)
  moveid = movie['imdb_id']
  #print(moveid)

  res = requests.get(f"https://api.themoviedb.org/3/find/{moveid}?api_key=1962248a00d2c9321120165be28b25c2&e41504150&external_source=imdb_id")
  #print(res.json())
  newPosterPath = res.json()['movie_results'][0]['poster_path']
  print(newPosterPath)
  
  mycollection.find_one_and_update({'_id': str(i)},{ '$set': { "poster_path" : newPosterPath} })


#for i in range(5143):
 #   updatePoster(i)
  #  print(i)

def startUpdating(start, end):
  for i in range(start, end, 1):
    print()
    #updatePoster(i)
   # print(i)





t1 = threading.Thread(target=startUpdating, args=[0, 10])
t2 = threading.Thread(target=startUpdating, args=[10, 20])
#t3 = threading.Thread(target=startUpdating, args=[10, 20])
#t4 = threading.Thread(target=startUpdating, args=[10, 20])

t1.start()
t2.start()

t1.join()
t2.join()

num_of_posters = 20
num_of_threads = 4
s1 = num_of_posters / 4
s2 = s1 + s1 
s3 = s2 + s1 
s4 = s3 + s1
print(s1, s2, s3, s4)