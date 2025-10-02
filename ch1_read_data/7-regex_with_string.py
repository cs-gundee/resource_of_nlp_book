# Шаардлагатай сангуудыг импортлох
import re
import requests

# Туршилтад ашиглах шүлгийн url
url = 'https://mn.wikipedia.org/wiki/%D0%9C%D0%B8%D0%BD%D0%B8%D0%B9_%D0%9D%D1%83%D1%82%D0%B0%D0%B3'

# текстийг задлах функц
def get_poem(url):
    # сайтаас шүлгийн текстийг авахын тулд http хүсэлт илгээх
    raw = requests.get(url).text

    # Текстийн эхлэлийг заах
    startText = re.search(r"Хэнтий", raw).end()
    
    # Авч буй текстийн төгсгөлийг заах
    stopText = re.search(r"Мэнэн", raw).start()
    
    # Заасан эхлэл, төгсгөлийн хооронд орших текстийг хадгалах
    text = raw[startText:stopText]
    return text

# Хадгалсан текстийг цааш боловсруулахад бэлтгэх
def preprocess(sentence): 
 	  return re.sub('[^А-Яа-яӨөЁёҮү0-9.]+' , ' ', sentence).lower()

# Текст задлах болох боловсруулах функцийг дуудаж ажиллуулах
poem = get_poem(url)
processed_poem = preprocess(poem)
print(processed_poem)

# Гаралт:
# хангай соёны өндөр сайхан нуруунууд хойд зүгийн чимэг болсон ойн хөвч уулнууд

# Текстэд орсон 'уул' үгийг тоолох
print(len(re.findall(r'уул', processed_poem)))

# Гаралт: 1

# preprocess() функцийн үр дүнд текстийн бүх үсгийг жижигрүүлсэн.
# Тэгвэл хангай үгийг томоор эхлүүлье.
processed_poem = re.sub(r'\sхангай\s', " Хангай ", processed_poem)
print(processed_poem)

# Гаралт: 
# Хангай соёны өндөр сайхан нуруунууд хойд зүгийн чимэг болсон ойн хөвч уулнууд

# [a,] хэлбэрийн бүх тохиолдлыг олох
t = re.findall(r'[А-Яа-яӨөЁёҮү0-9]*,', poem)
print(t)

# Гаралт:
# [',', 'Хангай,']

# з үсгээр эхэлсэн үгсийг олох
z = re.findall(r'\bз[А-Яа-яӨөЁёҮү]+', poem)
print(z)

# Гаралт: 
# ['зүгийн]

