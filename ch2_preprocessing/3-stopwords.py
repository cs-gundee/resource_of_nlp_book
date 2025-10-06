# жагсаалтыг data frame рүү хувиргах
import pandas as pd

text = ['This is introduction to NLP',
'It is likely to be useful, to people ',
'Machine learning is the new electrcity',
'There would be less hype around AI and more action going forward',
'python is the best tool!']

df = pd.DataFrame({'data':text})

# nltk санг суулгаж, импортлох
# !pip install nltk
import nltk
from nltk.corpus import stopwords

# Хэрэв анх удаа ажиллуулж байвал энэ мөрийг ажиллуулна:
nltk.download()


# Англи хэлний зогсоох үгсийг татах
stop = stopwords.words('english')

df['data'] = df['data'].apply(lambda x: " ".join(x for x in x.split() if x not in stop))
print(df['data'])

# Гаралт:
# 0                                This introduction NLP
# 1                             It likely useful, people
# 2                      Machine learning new electrcity
# 3    There would less hype around AI action going f...
# 4                                    python best tool!
# Name: data, dtype: object



import string

var_x = "Rokit Bay гэдэг нэр бол гурван өөр утгатай үгийг нэг үгэнд багтаасан юм. Хамгийн гол утга нь Rock it Bay буюу доргиогоод өг Bay гэсэн утгатай. Түүнийг Америкт байхад нэрийн эхний үеэр нь Bay гэж дууддаг байсан. Дараачийн нэг утга нь Rocket Bay буюу Пуужин Баяраа. Пуужин гэсний учир нь эрсдэлтэй боловч амжилттай хөөрвөл хэний ч хүрээгүй газар очно гэсэн утгатай. Харин сүүлийн утга нь Raw kit Bay буюу оригнал дуугаралттай гэсэн үг."

# Өөрийнхөөрөө хасах үгсийг тодорхойлох
stopwords = ['гэдэг', 'нь', 'юм', 'бол', 'буюу']

for s in stopwords:
    var_x = var_x.replace(s,"")
print(var_x)

# Гаралт:
# Rokit Bay  нэр  гурван өөр утгатай үгийг нэг үгэнд багтаасан . Хамгийн гол утга  Rock it Bay  доргиогоод өг Bay гэсэн утгатай. Түүнийг Америкт байхад нэрийн эхний үеэр  Bay гэж дууддаг байсан. Дараачийн нэг утга  Rocket Bay  Пуужин Баяраа. Пуужин гэсний учир  эрсдэлтэй овч амжилттай хөөрвөл хэний ч хүрээгүй газар очно гэсэн утгатай. Харин сүүлийн утга  Raw kit Bay  оригнал дуугаралттай гэсэн үг.
