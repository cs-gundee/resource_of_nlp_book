# Жишээ текст өгөгдөл
documents = (
	 "I like NLP",
	 "I am exploring NLP",
	 "I am a beginner in NLP",
	 "I want to learn NLP",
	 "I like advanced NLP"
)

# шаардлагатай сангуудыг импортлох
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# TF-IDF векторчлал хийх
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(documents)

print("TF-IDF матрицын хэмжээ:", tfidf_matrix.shape)

# Гаралт:
(5, 10) # 5 өгүүлбэр, 10 өвөрмөц үг

# Эхний өгүүлбэрийг бусад өгүүлбэртэй харьцуулан косинусын ижил төстэйг тооцоолох
cosine_similarity(tfidf_matrix[0:1],tfidf_matrix)

# Гаралт:
# array([[ 1. ,  0.17682765,  0.14284054,  0.13489366,   0.68374784]])
