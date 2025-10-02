# docx санг суулгах 
!pip install python-docx

# санг импортлох
from docx import Document

# Word файлтай ажиллах объект үүсгэх
doc = open("file.docx", "rb")

# Word файл унших объект үүсгэх
document = Document(doc)

# Хоосон string үүсгээд үүн дээр document -г дуудна.
# Энэ document хувьсагч нь Word файлын параграф бүрийг хадгална. 
# Харин давталт дотор дуудсанаар параграф бүрийг залгах боломжтой болно.
dc = ""
for par in document.paragraphs:
    dc += par.text 

# dc -г дуудаж үр дүнг хэвлэх
print(dc)
