!pip install textblob

# TextBlob санг дуудаж correct() функцийг ашиглах 
from textblob import TextBlob

var = ['ths', 'nama', 'ur', 'electrcity', 'intraduction']

for s in var:
  print(str(TextBlob(s).correct()))

var2 = 'I have a proccessing error in my sysem and its not wokring corectly'
print(TextBlob(var2).correct())

# Гаралт1: 
# the
# name
# or
# electricity
# introduction

# Гаралт2:
# I have a processing error in my system and its not working correctly

#============================================================================

# autocorrect санг суулгах
!pip install autocorrect

from autocorrect import Speller

# Speller объект үүсгэх (англи хэлний анхны тохиргоотой)
spell = Speller(lang='en')

# Алдаатай үгс
word1 = 'proccessing'
word2 = 'languge'

# Зөв бичгийн алдааг засах
print(spell(word1))
print(spell(word2))

# Гаралт: 
# processing
# language 


#============================================================================

# Бүтэн өгүүлбэр дээр ажиллуулах
sentence = "This sentense has some erors."

corrected_sentence = " ".join([spell(word) for word in sentence.split()])
print(corrected_sentence)

# Гаралт:
# This sentence has some errors.

