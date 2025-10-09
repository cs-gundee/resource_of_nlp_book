# шаардлагатай сангууд
from gensim.models import Word2Vec
from sklearn.decomposition import PCA
from matplotlib import pyplot

# жишээ өгүүлбэрүүд
sentences = [['I', 'love', 'nlp'],
            ['I', 'will', 'learn', 'nlp', 'in', '2','months'],
            ['nlp', 'is', 'future'],
            ['nlp', 'saves', 'time', 'and', 'solves', 'lot', 'of',
			  'industry', 'problems'],
            ['nlp', 'uses', 'machine', 'learning']]

#===========================================================================

# CBOW загвараар Word2Vec моделийг сургаж байна
# vector_size = 50 - үгийн векторын хэмжээ буюу бүрдэл хэмжээ 50
# window = 3 - төв үгийн өмнөх ба дараах 3 үгийг харгалзан сурах хүрээ
# min_count = 1 - хамгийн багадаа 1 удаа гарсан үгсийг сурах
# sg = 0 -> CBOW загварыг сонгох (skip-gram бол sg=1)
cbok = Word2Vec(
			sentences, 
			vector_size = 50, 
			window = 3, 
			min_count = 1, 
			sg = 0
)

# Моделийн товч мэдээллийг хэвлэх
print(cbok)

#===========================================================================

# Загварыг хадгалах
cbok.save('cbok.bin')

# Загварыг дуудах
cbok = Word2Vec.load('cbok.bin')

#===========================================================================

# Загварын үгийн бүх түлхүүр буюу үгсийн жагсаалт
words = list(cbok.wv.index_to_key)

# Үг бүрийн векторуудыг авах
X = cbok.wv[words]

# PCA-гаар хэмжээ бууруулах: 50 хэмжээст векторыг 2 хэмжээст болгоно
pca = PCA(n_components=2)
# PCA-г сургалтын векторуудад хэрэглэнэ
result = pca.fit_transform(X)

# 2D скаттер график байгуулах
pyplot.scatter(result[:, 0], result[:, 1])

# Цэг бүр дээр тухайн үгийг бичиж харуулах
for i, word in enumerate(words):
    pyplot.annotate(word, xy=(result[i, 0], result[i, 1]))

# Графикийг дэлгэцэд гаргах 
pyplot.show()

#===========================================================================

# gensim багцыг импортлох
from gensim.models import KeyedVectors

# Google-ийн урьдчилан бэлтгэсэн Word2Vec загварыг ачаалах
# Файл замыг өөрийн компьютерт байгаа байршилд тааруулна. Жишээ нь:
model_path = 'C:\\Users\\GoogleNews-vectors-negative300.bin'
model = KeyedVectors.load_word2vec_format(model_path, binary=True) 

#===========================================================================

# 'this' ба 'is' үгийн төстэй байдлыг шалгах
similarity_this_is = model.similarity('this', 'is')
print(similarity_this_is)
# Гаралт: 0.407970363878

# 'post' ба 'book' үгийн төстэй байдлыг шалгах
similarity_post_book = model.similarity('post', 'book')
print(similarity_post_book)
# Гаралт: 0.0572043891977

#===========================================================================

# оролтуудаас тохирохгүйг олох
odd_word = model.doesnt_match('breakfast cereal dinner lunch'.split())
print(odd_word)
# Гаралт: 'cereal'

# хоёр үгийн хоорондын харилцан хамаарлыг олох
result = word_vectors.most_similar(positive=['woman', 'king'], negative=['man'])
print(result)
# Гаралт:
# queen: 0.7699
