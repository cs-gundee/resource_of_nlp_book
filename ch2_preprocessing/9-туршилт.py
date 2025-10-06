import nltk
nltk.download('punkt')
nltk.download('webtext')

from nltk.corpus import webtext

# Firefox текст файлын өгүүлбэр ба үгсийг авах
wt_sentences = webtext.sents('firefox.txt')
wt_words = webtext.words('firefox.txt')

# Шаардлагатай сангууд
# Давтамж тооцоолоход хэрэглэх сангууд
from nltk.probability import FreqDist
from nltk.corpus import stopwords
import string

# Үгийн тоо шалгах
len(wt_sentences)
# Гаралт: 1144
len(wt_words)
# Гаралт: 102457

# Үгсийн давтамжийн тархалт үүсгэх
frequency_dist = nltk.FreqDist(wt_words) 

# Давтамжийг хэвлэх
print(frequency_dist)
# Гаралт: <FreqDist with 8296 samples and 102457 outcomes>

# Хамгийн их давтагдсан 5 үг
print(frequency_dist.most_common(5))
# Гаралт: [('.', 2428), ('in', 2203), ('to', 2130), ('"', 1971), ('the', 1762)]


sorted_frequency_dist = sorted(
    frequency_dist.items(), 
    key = lambda x: x[1], 
    reverse = True
)

print(sorted_frequency_dist) 
# Гаралт: [('.', 2428), ('in', 2203), ('to', 2130),…]

# 3-с дээш үсэгтэй үгсийг шүүж авах
large_words = dict([(k,v) for k,v in frequency_dist.items() if len(k)>3])

# Давтамжийг дахин тооцох
frequency_dist = nltk.FreqDist(large_words)

# Давтамжийн тархалтыг графикаар харах
# cumulative = False нь хуримтлагдсан биш, шууд давтамжийг харуулна
frequency_dist.plot(50, cumulative=False)


#========================================================================

# wordcloud санг суулгах
!pip install wordcloud

# сангуудыг импортлох
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# WordCloud үүсгэх
# frequency_dist (үг, давтамж) өгөгдлийг ашиглан үгэн үүлс байгуулна
wcloud = WordCloud(
    width = 800,            # Зургийн өргөн
    height = 400,           # Зургийн өндөр
    background_color = 'white'  # Дэвсгэрийн өнгө
).generate_from_frequencies(frequency_dist)

# WordCloud дүрслэх
plt.figure(figsize=(10, 5))           # Зургийн хэмжээ
plt.imshow(wcloud, interpolation='bilinear')  # Илүү зөөлөн дүрслэл
plt.axis("off")                       # Тэнхлэгүүдийг нуух
plt.show()

#========================================================================

import nltk
from nltk.corpus import stopwords, webtext
from nltk.probability import FreqDist
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import string

nltk.download('webtext')
nltk.download('stopwords')

wt_words = webtext.words('firefox.txt')

# Англи хэлний stopwords болон тэмдэгтийг устгах
stop_words = set(stopwords.words('english'))
clean_words = [
    w.lower() for w in wt_words
    if w.lower() not in stop_words and w.isalpha()
]

# Давтамжийн тархалт үүсгэх
frequency_dist = FreqDist(clean_words)

# WordCloud үүсгэх
wordcloud = WordCloud(
    width = 800,
    height = 400,
    background_color = 'white'
).generate_from_frequencies(frequency_dist)

# Зураг гаргах
plt.figure(figsize=(12, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
