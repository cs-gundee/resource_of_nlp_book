import numpy as np 
import nltk
from nltk import bigrams    
import itertools

# co-occurrence матриц үүсгэх функц тодорхойлох
def co_occurrence_matrix(corpus):
    vocab = set(corpus)
    vocab = list(vocab)
    vocab_to_index = { word:i for i, word in enumerate(vocab) }
    
    # корпус дахь бүх үгнээс bigram үүсгэх
    bi_grams = list(bigrams(corpus))

    # bigram -уудын давтамжийг тоолох ((word1, word2), num_occurrences)
    bigram_freq = nltk.FreqDist(bi_grams).most_common(len(bi_grams))
    
    # co-occurrence матрицыг үүсгэх
    # co_occurrence_matrix[current][previous]
    co_occurrence_matrix = np.zeros((len(vocab), len(vocab)))

    # bigram бүрээр давтаж co-occurrence тоог оруулах
    for bigram, count in bigram_freq:
        previous, current = bigram
        pos_previous = vocab_to_index[previous]
        pos_current = vocab_to_index[current]
        co_occurrence_matrix[pos_current][pos_previous] = count 
 
    co_occurrence_matrix = np.matrix(co_occurrence_matrix)

    # матриц болон үгийн индексийн толь буцаах
    return co_occurrence_matrix, vocab_to_index


import pandas as pd
# туршилтын өгөгдөл
sentences = [['I', 'love', 'nlp'],
            ['I', 'love','to' 'learn'],
            ['nlp', 'is', 'future'],
            ['nlp', 'is', 'cool']]

# олон жагсаалтыг нэг жагсаалт болгон нэгдүүлэх
merged = list(itertools.chain.from_iterable(sentences)) 

# co-occurrence матриц үүсгэх
matrix, vocab_index = co_occurrence_matrix(merged)

# үр дүнг датафреймээр харах
# vocab_index бол үгийн индексийн толь
CoMatrixFinal = pd.DataFrame(matrix, index=vocab_index.keys(), columns=vocab_index.keys())
print(CoMatrixFinal)
