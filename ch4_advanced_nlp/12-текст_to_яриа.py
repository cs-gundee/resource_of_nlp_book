# gTTS санг суулгах
!pip install gTTS

from gtts import gTTS

# Хөрвүүлэх өгөгдөл
text_to_convert = 'I like this NLP book'

# Хэл сонгох, Англи хэл бол - 'en' 
# slow=False бол хурдан, slow=True бол удаан уншина
convert = gTTS(text= text_to_convert, lang='en', slow=False) 
  
# Хөрвүүлсэн аудиог mp3 файл болгон хадгалах
convert.save("audio.mp3")

# Гаралт: "audio.mp3" файлыг хадгалсан хавтаснаасаа сонсоно.
