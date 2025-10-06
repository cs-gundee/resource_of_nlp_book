import pandas as pd
from textblob import TextBlob

import nltk
nltk.download('punkt_tab')

text = ['L.A. on a Saturday night in the summer',
        'Sundown and they all come out',
        'Lamborghinis and their rented Hummers']

df = pd.DataFrame({'lyric': text})

TextBlob(df['lyric'][1]).words
# Гаралт
# WordList(['Sundown', 'and', 'they', 'all', 'come', 'out'])

#============================================================

df['words'] = df['lyric'].apply(lambda x: TextBlob(x).words)
print(df['words'])

#============================================================

import nltk

mystring = "Sundown and they all come out"

nltk.word_tokenize(mystring)

# Гаралт:
# ['Sundown', 'and', 'they', 'all', 'come', 'out']

#============================================================

mystring = "Sundown and they all come out"

mystring.split()

# Гаралт:
# ['Sundown', 'and', 'they', 'all', 'come', 'out']
