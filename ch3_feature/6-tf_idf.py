# TfidfVectorizer импортлох
from sklearn.feature_extraction.text import TfidfVectorizer

text = ["The quick brown fox jumped over the lazy dog.",
"The dog.",
"The fox"]

# Векторжуулагч үүсгэх
vectorizer = TfidfVectorizer()

#Текстийг токен болгон хувиргах ба сургах
vectorizer.fit(text)

# Тохируулагдсан үгийн сан (vocabulary) болон үгийн IDF утгуудыг хэвлэх
print(vectorizer.vocabulary_)	# Үгийн индексийн толь
print(vectorizer.idf_)	# Үг бүрийн IDF утга

# Гаралт:
# {'the': 7, 'quick': 6, 'brown': 0, 'fox': 2, 'jumped': 3, 'over': 5, 'lazy': 4, 'dog': 1}
# [1.69314718 1.28768207 1.28768207 1.69314718 1.69314718 1.69314718
#  1.69314718 1.        ]
