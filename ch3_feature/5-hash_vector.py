from sklearn.feature_extraction.text import HashingVectorizer

# туршилтын өгөгдөл
text = ["The quick brown fox jumped over the lazy dog."]

# 10 хэмжээтэй (n_features=10) хэш векторжуулагч үүсгэх
vectorizer = HashingVectorizer(n_features=10)

# Текстийг хэш вектор болгон хувиргах
vector = vectorizer.transform(text)

# Векторыг харуулах
print(vector.shape)	# Векторын хэмжээ (1 мөр, 10 багана)
print(vector.toarray())	# Векторыг массив болгон хэвлэх

# Гаралт:
# (1, 10)
# [[ 0.   0.57735027  0.  0.  0.  0.  0.  -0.57735027     -0.57735027     0.]]
