# Товчилсон үгсийн тайлбар толь
lookup_dictionary = {
    'nlp': 'natural language processing',
    'бна': 'байна',
    'сайн2': 'сайн сайн'
}

import re

# текстийг стандартчилах зорилготой функц
def text_std(input_text):
 words = input_text.split()
 new_words = []

 for word in words: 
     # Тусгай тэмдэгтүүдийг арилгах (асуултын тэмдэг, цэг гэх мэт)
     word = re.sub(r'[^\w\s]', '', word)

     if word.lower() in lookup_dictionary:
         word = lookup_dictionary[word.lower()]
         new_words.append(word)
         new_text = " ".join(new_words)
 return new_text

print(text_std("nlp"))
# Гаралт: natural language processing

print(text_std("Бна уу? Сайн уу?"))
# Гаралт: байна

print(text_std("Сайн2"))
# Гаралт: сайн сайн
