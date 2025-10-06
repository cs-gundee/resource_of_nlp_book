import nltk
nltk.download('punkt_tab')
# textblob санг импортлох
from textblob import TextBlob

text = "I am learning NLP"

# n = 1 тохиолдол буюу unigram үүсгэх
TextBlob(text).ngrams(1)

# Гаралт:
# [WordList(['I']), WordList(['am']), WordList(['learning']), WordList(['NLP'])]



# n = 2 тохиолдол буюу bigram үүсгэх
TextBlob(text).ngrams(2)

# Гаралт:
# [WordList(['I', 'am']),
# WordList(['am', 'learning']),
# WordList(['learning', 'NLP'])]


from sklearn.feature_extraction.text import CountVectorizer

text = ["I love NLP and I will learn NLP in 2month "]

# CountVectorizer-ийг bigram-ийг үүсгэхээр тохируулах
vectorizer = CountVectorizer(ngram_range=(2, 2))

# Текст дэх bigram-уудыг суралцаж, үгийг индексжүүлэх
vectorizer.fit(text)

# Текстийг тоологч вектор руу хөрвүүлэх
vector = vectorizer.transform(text)

# Үүссэн bigram үгс болон тэдгээрийн индексийг хэвлэх
print(vectorizer.vocabulary_)

# Текстэд bigram үгс хэдэн удаа давтагдсан тоог массив хэлбэрээр хэвлэх
print(vector.toarray())

# Гаралт:
# {'love nlp': 3, 'nlp and': 4, 'and will': 0, 'will learn': 6, 'learn nlp': 2, 'nlp in': 5, 'in 2month': 1} 
# [[1 1 1 1 1 1 1]]
