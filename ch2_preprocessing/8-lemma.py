text = ['fish', 'fishes', 'leaves', 'leaf']

# шаардлагатай санг импортлох
from textblob import Word 
import nltk
nltk.download('wordnet')

for word in text:
  print(Word(word).lemmatize())

# Гаралт: 
# fish
# fish
# leaf
# leaf
