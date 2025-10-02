import re

pattern = r'сайн'
text = 'Сайн байна уу?'

result = re.search(pattern, text, re.I)  

# import re

text = "Python is powerful"
result = re.match(r'Python', text)

if result:
    print("Амжилттай олдлоо:", result.group())
else:
    print("Олдсонгүй.")
# Амжилттай олдлоо: Python

# import re

text = "I love Python programming"
result = re.search(r'Python', text)

if result:
    print("Хайлт олдлоо:", result.group())
else:
    print("Хайлт амжилтгүй.")
# Хайлт олдлоо: Python

# Санг импортлох
# import re

# Эх өгүүлбэр
sentence = 'Ахаа алд хүндэл.'

# Өгүүлбэрийг үгс болгон хуваах
re.split('\W+', sentence)

# ['Ахаа', 'алд', 'хүндэл', '']

tokens = list(filter(None, re.split('\W+', sentence)))
print(tokens)
# ['Ахаа', 'алд', 'хүндэл']

# import re

# Имэйл хайх текст өгөгдөл
text = "Холбоо барих: contact@lend.mn 77070101 Та өөрийн дэлгэрэнгүй анкетаа people@andsystems.net хаягруу илгээнэ үү."

# Имэйл хэлбэрийг хайх регуляр илэрхийлэл
allmail = re.findall(r'[\w\.-]+@[\w\.-]+', text)

# Олдсон имэйл хаягуудыг хэвлэх
for mail in allmail: 
    print(mail)

# Гаралт: 
# contact@lend.mn 
# people@andsystems.net

# import re

# Имэйл солих текст өгөгдөл
text = "Холбоо барих: contact@lend.mn 77070101 Та өөрийн дэлгэрэнгүй анкетаа people@andsystems.net хаягруу илгээнэ үү."

# Олдсон имэйл хаягуудыг солих
new_email_address = re.sub(r'([\w\.-]+)@([\w\.-]+)', r'contact@lend.com', text)

# Хэвлэх
print(new_email_address)

# Гаралт:
# Холбоо барих: contact@lend.com 77070101 Та өөрийн дэлгэрэнгүй анкетаа contact@lend.com хаягруу илгээнэ үү.

