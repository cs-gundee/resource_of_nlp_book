# Жишээ өгөгдөл
Text1 = 'I went to the bank to deposit my money'
Text2 = 'The river bank was full of dead fishes'



# pywsd санг суулгах
!pip install pywsd

# Шаардлагатай сангуудыг татаж авах
import nltk
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
nltk.download('punkt')

# Холбогдох функцуудыг импортлох
from pywsd.lesk import simple_lesk



# Өгүүлбэрүүдийг нэгтгэх
bank_sents = [Text1, Text2]



nltk.download('punkt_tab')
# Эхний өгүүлбэрийг хэвлэх
print ("Context-1:", bank_sents[0])

# Леск алгоритм ашиглан "bank" үгийн утгыг тодорхойлох
answer = simple_lesk(bank_sents[0], 'bank')

# Үр дүнг хэвлэх
print ("Sense:", answer)
print ("Definition : ", answer.definition())

# Гаралт:
# Context-1: I went to the bank to deposit my money 
# Sense: Synset(‘depository_financial_institution.n.01’) 
# Definition :  a financial institution that accepts deposits and channels the money into lending activities




# Хоёр дахь өгүүлбэрийг хэвлэх
print ("Context-2: ", bank_sents[1])

# Lesk функцийг дуудаж ажиллуулах
# ‘n’ буюу нэр үгийн утгаар тодорхойлохыг зааж өгч байна
answer = simple_lesk(bank_sents[1], 'bank', 'n')

# Үр дүнг гаргах
print ("Sense: ", answer)
print ("Definition: ", answer.definition())

# Гаралт:
# Context-2: The river bank was full of dead fishes 
# Sense: Synset('bank.n.01') 
# Definition :  sloping land (especially the slope beside a body of water)
