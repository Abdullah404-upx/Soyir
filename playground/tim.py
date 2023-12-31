

import re

from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from nltk.tokenize import word_tokenize


def cleanText(text_data, stopwordss=True, stemming=True):

	stopWords = set(stopwords.words("english"))
	ps = SnowballStemmer('english')

	# Tokenize text contents
	contents = word_tokenize(text_data)

	# To store the corpus of words
	corpus = list()

	# Create corpus, remove special chars and lowercase operation.
	for content in contents:

		content = re.sub('[^A-Za-z0-9]+', '', content).lower()
		corpus.append(content)

	# Remove Stopwords before stemming
	corpus = [word for word in corpus if word not in stopWords]

	#  Snowball Stemmer
	corpus = [ps.stem(word) for word in corpus]

	# remove stopwords after stemming
	corpus = [word for word in corpus if word not in stopWords]

	# Remove unnecessary empty strings from corpus
	corpus = [word for word in corpus if word != '' and len(word) > 2]

	# Convert back to string
	#corpus = " ".join(corpus)
    
# Clean the text
	# text = re.sub(r"[^A-Za-z0–9^,!.\/'+-=]", " ", text)
	# text = re.sub(r"what's", "what is ", text)
	# text = re.sub(r"\'s", " ", text)
	# text = re.sub(r"\'ve", " have ", text)
	# text = re.sub(r"can't", "cannot ", text)
	# text = re.sub(r"n't", " not ", text)
	# text = re.sub(r"i'm", "i am ", text)
	# text = re.sub(r"\'re", " are ", text)
	# text = re.sub(r"\'d", " would ", text)
	# text = re.sub(r"\'ll", " will ", text)
	# text = re.sub(r",", " ", text)
	# text = re.sub(r"\.", " ", text)
	# text = re.sub(r"!", " ! ", text)
	# text = re.sub(r"\/", " ", text)
	# text = re.sub(r"\^", " ^ ", text)
	# text = re.sub(r"\+", " + ", text)
	# text = re.sub(r"\-", " - ", text)
	# text = re.sub(r"\=", " = ", text)
	# text = re.sub(r"'", " ", text)
	# text = re.sub(r"(\d+)(k)", r"\g<1>000", text)
	# text = re.sub(r":", " : ", text)
	# text = re.sub(r" e g ", " eg ", text)
	# text = re.sub(r" b g ", " bg ", text)
	# text = re.sub(r" u s ", " american ", text)
	# text = re.sub(r"\0s", "0", text)
	# text = re.sub(r" 9 11 ", "911", text)
	# text = re.sub(r"e - mail", "email", text)
	# text = re.sub(r"j k", "jk", text)
	# text = re.sub(r"\s{2,}", " ", text)
	return corpus

q = "this is the most passive 9999 and. 2007 10"
#print(cleanText(q))
q = '"the good person"'
if q.startswith('"') and q.endswith('"'):
	q = q[1:-1]
print(q)