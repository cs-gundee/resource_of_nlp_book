# Жишээ баримт үүсгэх
doc1 = "I am learning NLP, it is very interesting and exciting. it includes machine learning and deep learning" 
doc2 = "My father is a data scientist and he is nlp expert"
doc3 = "My sister has good exposure into android development"

doc_complete = [doc1, doc2, doc3] 
print(doc_complete)


# шаардлагатай сангуудыг суулгах
!pip install gensim
import nltk
nltk.download('stopwords')
nltk.download('wordnet')

from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
import string

# Stopwords буюу утга багатай түгээмэл үгсийн жагсаалтыг авах
stop = set(stopwords.words('english'))

# Цэг таслал, тэмдэгтүүдийн жагсаалт
exclude = set(string.punctuation) 

# Үгсийг үндсэн хэлбэрт буцаах lemmatizer үүсгэх
lemma = WordNetLemmatizer()

# Текстийг урьдчилан цэвэрлэх функц
def clean(doc):
    # Текстийг жижиг үсгээр бичиж, stopwords-ийг устгана
    stop_free = " ".join([i for i in doc.lower().split() if 
i not in stop])
   
	  # Тэмдэгтүүдийг устгана
    punc_free = ''.join(ch for ch in stop_free if ch not in exclude)
   
	  # Үг бүрийг үндсэн хэлбэрт нь шилжүүлнэ
    normalized = " ".join(lemma.lemmatize(word) for word in punc_free.split())
    return normalized

# Бүх баримтуудыг цэвэрлэж, үгсийн жагсаалт хэлбэрт оруулах
doc_clean = [clean(doc).split() for doc in doc_complete]  

# Цэвэрлэсэн өгөгдлийг хэвлэх
print(doc_clean)

# Гаралт:
# [['learning',  'nlp',  'interesting',  'exciting',  
#   'includes',  'machine',  'learning',  'deep',  'learning'], 
#   ['father', 'data', 'scientist', 'nlp', 'expert'], 
#   ['sister', 'good', 'exposure', 'android', 'development']]


# gensim санг импортлох
import gensim
from gensim import corpora

# Өгөгдсөн цэвэрлэсэн баримтуудаас (doc_clean) 
# өвөрмөц үг бүрт индекс оноож, нэр томъёоны толь бичгийг үүсгэх
dictionary = corpora.Dictionary(doc_clean)

# Үүсгэсэн толь бичгийг ашиглан баримтын жагсаалтаас
# Document-Term матриц буюу корпус үүсгэх
doc_term_matrix = [dictionary.doc2bow(doc) for doc in doc_clean]

# Корпусыг хэвлэх
print(doc_term_matrix)

# Гаралт:
# [[(0, 1), (1, 1), (2, 1), (3, 1), (4, 3), (5, 1), (6, 1)], 
#  [(6, 1), (7, 1), (8, 1), (9, 1), (10, 1)], 
#  [(11, 1), (12, 1), (13, 1), (14, 1), (15, 1)]]


# gensim сангаас LDA загвар үүсгэх классийг авах
Lda = gensim.models.ldamodel.LdaModel

# LDA загварыг сургах ба ажиллуулах
# num_topics = 3: 3 сэдэвтэй загвар үүсгэнэ
# id2word = dictionary: үгсийн индексийг зааж өгнө
# passes = 50: өгөгдлийг 50 удаа давтан суралцана
ldamodel = Lda(doc_term_matrix, num_topics=3, id2word=dictionary, passes=50)

# Сурсан загварын сэдвүүдийг хэвлэх
print(ldamodel.print_topics())

# Гаралт: [(0, '0.173*"learning" + 0.121*"nlp" + 0.069*"deep" + 0.069*"exciting" + 0.069*"interesting" + 0.069*"includes" + 0.069*"machine" + 0.069*"scientist" + 0.069*"data" + 0.069*"expert"'), (1, '0.129*"development" + 0.129*"exposure" + 0.129*"good" + 0.129*"sister" + 0.129*"android" + 0.032*"expert" + 0.032*"scientist" + 0.032*"data" + 0.032*"father" + 0.032*"nlp"'), (2, '0.063*"data" + 0.063*"scientist" + 0.063*"father" + 0.063*"expert" + 0.063*"nlp" + 0.062*"interesting" + 0.062*"deep" + 0.062*"exciting" + 0.062*"includes" + 0.062*"machine"')]
