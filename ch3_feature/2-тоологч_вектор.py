# scikit сангаас импортлох
from sklearn.feature_extraction.text import CountVectorizer

# Текст өгөгдөл
text = ["I love NLP and I will learn NLP in 2month "]

# CountVectorizer объект үүсгэх
vectorizer = CountVectorizer()

# Текстийг токенжуулж, үгийн санг бүрдүүлэх
vectorizer.fit(text)

# Текстийг тоологч вектор руу хөрвүүлэх
vector = vectorizer.transform(text)

# Үгийн сан (vocabulary) буюу токенуудын индексүүдийг хэвлэх
print(vectorizer.vocabulary_)

# Тоологч векторын массивыг хэвлэх
print(vector.toarray())

# Гаралт:
# {'love': 4, 'nlp': 5, 'and': 1, 'will': 6, 'learn': 3, 'in': 2, '2month': 0} 
# [[1 1 1 1 1 2 1]]
