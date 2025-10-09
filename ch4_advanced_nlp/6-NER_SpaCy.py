# spacy санг импортлох
import spacy

# Англи хэлний жижиг загварыг ачаалах
nlp = spacy.load("en_core_web_sm")

# Жишээ өгүүлбэр
doc = nlp("Apple is ready to launch new phone worth $10000 in New York Time Square")

# NER үр дүнг хэвлэх
for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)

# Гаралт:
# Apple 0 5 ORG 
# 10000 42 47 MONEY 
# New york 51 59 GPE
