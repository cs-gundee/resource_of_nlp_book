# Шаардлагатай сангуудыг импортлох
import nltk
nltk.download('stopwords') 
nltk.download('averaged_perceptron_tagger')
nltk.download('averaged_perceptron_tagger_eng')
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize, sent_tokenize 

# Англи хэлний зогсоох үгсийг тодорхойлох
stop_words = set(stopwords.words('english')) 

# Жишээ өгөгдөл
text  =  "I love NLP and I will learn NLP in 2 month"

# Өгүүлбэрээр тасалж, тэмдэглэгээ үүсгэх
tokens = sent_tokenize(text) 

# давталт ашиглан тэмдэглэгээ үүсгэх
for sentence in tokens:
    words = word_tokenize(sentence)
    
    # Зогсоох үгсийг устгах
    filtered_words = [w for w in words if w.lower() not in stop_words]
    
    # POS тэмдэглэгээ хийх
    tags = nltk.pos_tag(filtered_words)
    print(tags)

# Гаралт:
# [('love', 'NN'), ('NLP', 'NNP'), ('learn', 'NN'), ('NLP', 'NNP'), ('2', 'CD'), ('month', 'NN')]
