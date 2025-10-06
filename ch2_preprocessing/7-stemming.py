text = ['I like fishing', 'I eat fish', 'There are many fishes in pound']

import pandas as pd
from nltk.stem import PorterStemmer

# Датафрейм үүсгэх
df = pd.DataFrame({'st':text})

# Stemming хийх объект
st = PorterStemmer()

# Датафреймийн 'st' баганын текст бүрт stemming хийх
df['stemmed'] = df['st'].apply(lambda x: " ".join([st.stem(word) for word in x.split()]))

print(df['stemmed'])

# Гаралт:
# 0                     I like fish
# 1                      I eat fish
# 2    there are mani fish in pound
