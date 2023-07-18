# import rapidfuzz
# import ipywidgets as widgets 
# from rapidfuzz import process as rapidfuzz_process 
# docs = ["star warz", "start shit", "start kick", "the one of the sht", "simple biblmbe", "simply wimbly", "this is a very simply type a word  good thing", "this is not a very good thing", "life is life"]

# def suggest(query):
#   if not query: return 
#   #print(rapidfuzz_process.extract(query, docs, limit=10))
#   for i, score, _ in rapidfuzz_process.extract(query, docs, limit=7, score_cutoff=90):
#     print(i, score)
# suggest('this is')

# widgets.interact(suggest, query="")
a =["1", "2", "3", "hhh", "a", "aaa"]
dimINdex = a.index("hhh")
print("gdasg a7a".count("a7a"))
document = ['', '']
document[0] = [a[0:dimINdex]]
document[1] = [a[dimINdex+1:]]
print(document)


print(" ".join(a))