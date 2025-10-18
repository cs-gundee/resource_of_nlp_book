# Жишээ өгөгдөл
text = "Bonjour le monde"

# Орчуулах объект үүсгэх
gs = goslate.Goslate()

# Англи хэл рүү орчуулах
translatedText = gs.translate(text, 'en')

print(translatedText)

# Гаралт:
# Hello world
