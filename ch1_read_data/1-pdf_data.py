!pip install PyPDF2
import PyPDF2
from PyPDF2 import PdfFileReader

# PDF файлтай ажиллах объект үүсгэх
pdf = open("filename.pdfx", "rb")
 
# PDF файл унших объект үүсгэх
pdf_reader = PyPDF2.PdfReader(pdf)

# PDF файлын хуудасны тоог шалгах
print(len(pdf_reader.pages))

# Эхний хуудсыг дуудаж, хуудас объект үүсгэх
page = pdf_reader.pages[0]

# Хуудаснаас текст задалж авах
print(page.extract_text())

# PDF файлыг хаах
pdf.close()
