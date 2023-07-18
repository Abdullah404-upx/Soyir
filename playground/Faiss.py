import pandas as pd
import faiss 
# d = sBert().dimensions
# print(d)
# cells = 4
# quantizer = faiss.IndexFlatL2(d) # l dstiacne 
def FaissFlatL2():

    index = faiss.IndexFlatL2(bertModel.dimensions)
    index = faiss.IndexIDMap(index)

    import pandas as pd
    l = [1, 2, 3, 4, 5]
    df = pd.DataFrame({'age':    l})


    print(df.age.values)


    index.add_with_ids(bertModel.sentence_embeddings, df.age.values)

def FaissIV():
    
    cells = 2 # num of cells you want in your vironar
    d = bertModel.dimensions
    quantizer = faiss.IndexFlatL2(d)
    index = faiss.IndexIVFFlat(quantizer, d, cells)
    index.train(bertModel.sentence_embeddings)

    
    l = [1, 3, 9, 4, 5]
    df = pd.DataFrame({'age':    l})
        # print(df.age.values)
        # ids = df.age.values
        # ids = np.arange(bertModel.sentence_embeddings.shape[0])
    index.add_with_ids(bertModel.sentence_embeddings, df.age.values)
    num_of_IndexedVecs= index.ntotal
    faiss.write_index(index, 'ag')
    print("trained and saved")
    # 
    nprobe = 5
    # load and then search
    D, I = index.search(xq, 2)
    print(I)


		function Highlighter(){

		}
		function Poster(val){
			console.log(val, 'HELLLLLLLLLLLLL')
			console.log("hi therhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhe")
			fetch(`https://api.themoviedb.org/3/find/tt0114709?api_key=1962248a00d2c9321120165be28b25c2&e41504150&external_source=imdb_id`)
			.then(res=> res.json()).then(data => {
				console.log(data['movie_results'][0]['poster_path'])
				path = `https://image.tmdb.org/t/p/w500/${data['movie_results'][0]['poster_path']}`
				document.getElementById("box").setAttribute("src",path);
			})
			

		
		}