# BeautifulSoup суулгах
!pip install beautifulsoup4 

# Сангуудыг импортлох
import urllib.request
from bs4 import BeautifulSoup

# Веб хуудасны хаягийг зааж өгнө
url = 'https://mn.wikipedia.org/wiki/%D0%A5%D1%8D%D0%BB_%D1%8F%D1%80%D0%B8%D0%B0%D0%BD%D1%8B_%D1%85%D0%B8%D0%B9%D0%BC%D1%8D%D0%BB_%D0%BE%D1%8E%D1%83%D0%BD'

# Header тодорхойлох
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122 Safari/537.36'}

# #  Хаяг руу HTTP хүсэлт илгээж, хариуг авна
req = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(req)

# Хариу болгон ирсэн HTML агуулгыг уншиж авна
html_doc = response.read()

# BeautifulSoup ашиглан HTML агуулгыг задлах
soup = BeautifulSoup(html_doc, 'html.parser')

# Эмх цэгцтэй хэлбэрт хөрвүүлэх
str_html = soup.prettify()

# Цөөн хэдэн өгөгдлийг хэвлэх
# Хязгаарыг өөрийн хүссэнээр олгож болно.
print(str_html[:200])

# <title> тагийг хэвлэх
print(soup.title)

# <title> тагийн утгыг хэвлэх
print(soup.title.string) 

# эхний <а> тагийн утгыг хэвлэх
print(soup.a.string)

# <b> тагийн утгыг хэвлэх
print(soup.b.string)

for tag in soup.find_all(['h1', 'h2', 'h3']): 
	print(tag.text)

for x in soup.find_all('p'): 
	print(x.text)
