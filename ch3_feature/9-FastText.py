# gensim-ийн FastText загварыг ашиглах
from gensim.models import FastText

# PCA (Principal Component Analysis) ашиглан векторын хэмжээг бууруулах
from sklearn.decomposition import PCA

# Matplotlib ашиглан үгийн векторыг дүрслэх
from matplotlib import pyplot

# Жишээ өгүүлбэрүүд
sentences = [['I', 'love', 'nlp'],
            ['I', 'will', 'learn', 'nlp', 'in', '2', 'months'],
            ['nlp', 'is', 'future'],
            ['nlp', 'saves', 'time', 'and', 'solves', 'lot', 'of', 'industry', 'problems'],
            ['nlp', 'uses', 'machine', 'learning']]

# FastText загвар үүсгэх
fast = FastText(
    sentences,       # Сургалтын өгөгдөл (өгүүлбэрүүдийн жагсаалт)
    vector_size = 20,  # Үгийн векторыг 20 хэмжээст болгох
    window = 1,        # Нэг үгнээс баруун/зүүн тал руу харах үгийн тоо
    min_count = 1,     # Давтамж 1-ээс бага үгийг хасахгүй
    workers = 5,       # CPU-ийн 5 цөм ашиглах
    min_n = 1,         # Subword-ийн хамгийн бага урт
    max_n = 2          # Subword-ийн хамгийн их урт
)

# ‘nlp’ үгийн векторыг авах
print(fast.wv['nlp'])

# 'deep' үгийн векторыг авах
print(fast.wv['deep'])

# from gensim.models import Word2Vec
fast.save('fast.bin')

# Загварыг дахин дуудах
fast = FastText.load('fast.bin')

# Загварт байгаа бүх үгийн жагсаалт авах
words = list(fast.wv.index_to_key)

# Үгийн векторуудыг авах
X = fast.wv[words]

# PCA ашиглан 2 хэмжээст болгон бууруулах
pca = PCA(n_components=2)
result = pca.fit_transform(X)

# Скаттер диаграм байгуулах
pyplot.scatter(result[:, 0], result[:, 1])

# Үг бүрийг график дээр бичих
for i, word in enumerate(words):
    pyplot.annotate(word, xy=(result[i, 0], result[i, 1]))

pyplot.show()
