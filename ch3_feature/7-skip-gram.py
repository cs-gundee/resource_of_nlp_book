# жишээ өгүүлбэрүүд
sentences = [['I', 'love', 'nlp'],
            ['I', 'will', 'learn', 'nlp', 'in', '2','months'],
            ['nlp', 'is', 'future'],
            ['nlp', 'saves', 'time', 'and', 'solves', 'lot', 'of', 
        'industry', 'problems'],
            ['nlp', 'uses', 'machine', 'learning']]

#=============================================

# шаардлагатай сангуудыг суулгаж, импортлох
!pip install gensim

from gensim.models import Word2Vec

# Skip-Gram сургалтын загвар 
skipgram = Word2Vec(
    sentences, 
    vector_size = 50, 
    window = 3, 
    min_count = 1, 
    sg = 1
)
print(skipgram)

# 'nlp' үгэнд зориулсан вектор
print(skipgram.wv['nlp'])


#=============================================

# deep үгэнд зориулсан вектор руу хандах
print(skipgram.wv['deep'])

# Гаралт:
# KeyError: “word ‘deep’ not in vocabulary”

#=============================================

# Загварыг хадгалах
skipgram.save('skipgram.bin')

# Загварыг дуудах
skipgram = Word2Vec.load('skipgram.bin')

#=============================================

from sklearn.manifold import TSNE
import matplotlib.pyplot as plt 

# skipgram.wv.index_to_key - сурсан үгийн жагсаалт
words = list(skipgram.wv.index_to_key)

# Үг бүрийн векторуудыг авч байна
X = skipgram.wv[words]

# t-SNE хэрэглэх
# n_components = 2 - 2 хэмжээст рүү бууруулах
# random_state = 42 - үр дүнг тогтвортой гаргахын тулд
# perplexity = 5 - ойрын хөршүүдийн тоог тохируулж байна, жижиг өгөгдөлд бага утга тохиромжтой
tsne = TSNE(n_components=2, random_state=42, perplexity=5)
result = tsne.fit_transform(X)

# Скаттер график үүсгэх
plt.figure(figsize=(12, 8)) # Зургийн хэмжээ
plt.scatter(result[:, 0], result[:, 1]) # # t-SNE-ээр гарсан координатууд дээр цэгүүд зурах

# График дээр үгсийг байрлуулах (аннотаци хийх)
for i, word in enumerate(words):
  plt.annotate(word, xy=(result[i, 0], result[i, 1]))

# График харуулах
plt.show()

#=============================================
