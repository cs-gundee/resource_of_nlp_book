# Сангууд суулгах 
!pip install bs4
!pip install requests

# Импортлох шаардлагатай сангууд
from bs4 import BeautifulSoup
import requests

# Өгөгдөл авах холбоос хаяг
url = 'https://internom.mn/charts/internom-top100'

# Хуурамч хөтчийн мэдээлэл илгээж bot хамгаалалтаас зайлсхийх
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

# Хүсэлт илгээж хуудасны агуулгыг авах
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, "lxml")

books = soup.find_all('div', {'class':'w-full col-span-6 md:col-span-4 xl:col-span-3'})

booktitles = []
authors = []
prices = []

# books жагсаалтын эхний 10 ном дээр давталт хийнэ
for book in books[:10]:
    # Гарчиг агуулах class="text-sm" бүхий div элементийг хайна
    title_column = book.find("div", class_="text-sm")
    
    # Зохиогчийн нэр агуулах class="font-light" бүхий span элементийг хайх
    author_column = book.find("span", class_="font-light")

    # Үнэ агуулах class="font-medium md:text-lg" бүхий div элементийг хайх
    price_column = book.find("div", class_="font-medium md:text-lg")
    
    # Гарчиг агуулах мөрөөс текстийг авч, илүү зайг арилгана
    title = title_column.text.strip()
   
		 # Гарчгийг booktitles жагсаалтад нэмнэ
    booktitles.append(title)
    
    # Зохиогчийн нэр агуулах мөрөөс нэрийг авч, илүү зайг арилгана
    author = author_column.text.strip()
    # Зохиогчийн нэрийг authors жагсаалтад нэмнэ
    authors.append(author)

    # Үнийн мэдээллийг span дотроос авч, илүү зайг арилгана
    price = price_column.span.text.strip()
    
    # Үнийг prices жагсаалтад нэмнэ
    prices.append(price)

    # Номын нэр, зохиогч, үнийг хамт хэвлэнэ
    print(f"{title} ({author}) - Үнэ: {price}")


# pandas сан болон түүний Series, DataFrame классуудыг импортолж байна
import pandas as pd
from pandas import Series, DataFrame

# Номын нэрсийг Series төрөлд хувиргаж байна
booktitles = Series(booktitles)

# Зохиогчийн нэрсийг Series төрөлд хувиргаж байна
authors = Series(authors)

# Үнийн мэдээллийг Series төрөлд хувиргаж байна
prices = Series(prices)

# Гурван Series-г багануудаар нь нэгтгэж DataFrame үүсгэж байна (axis=1 → баганаар нийлүүлнэ)
book_dataframe = pd.concat([booktitles, authors, prices], axis=1)

# DataFrame-ийн багануудын нэрийг тодорхой, монгол хэлээр тохируулж өгнө
book_dataframe.columns = ['Номын нэр', 'Зохиогч', 'Үнэ']

# DataFrame-д 'Байр' нэртэй шинэ багана нэмэх ба индекс дээр тулгуурлан эрэмбэлнэ
book_dataframe['Байр'] = book_dataframe.index + 1

# Эхний 3 номын мэдээллийг хүснэгт байдлаар хэвлэж байна
book_dataframe.head(3)
