# Шаардлагатай сангуудыг импортлох ба татаж авах
import nltk
nltk.download('brown')    # TextBlob ажиллахад шаардлагатай өгөгдлийн сан
nltk.download('punkt_tab')    # Текст задлахад ашиглагдах сан
from textblob import TextBlob

# Нэр хэлцийг ялгах жишээ
blob = TextBlob("John is learning natural language processing")
for np in blob.noun_phrases:
    print(np)

# Гаралт: 
#   John
#   natural language processing
