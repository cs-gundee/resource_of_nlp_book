# Шаардлагатай сангуудыг импортлох
import numpy as np                  # Тоон өгөгдлийн боловсруулалт
import pandas as pd                 # Өгөгдөл унших, боловсруулах
import matplotlib.pyplot as plt     # Харагдац (visualization) үүсгэх

# Өгөгдлийг унших
df = pd.read_csv(‘Reviews.csv’)     # Reviews.csv файлыг уншиж, DataFrame-д хадгалах

# Эхний 5 мөрийг харах
df.head(5)



# Багана бүрийн өгөгдлийн төрлийг харах
df.info()

# Гаралт:
    # Data columns (total 10 columns): 
    # Id                        5 non-null int64 
    # ProductId                 5 non-null object 
    # UserId                    5 non-null object 
    # ProfileName               5 non-null object 
    # HelpfulnessNumerator      5 non-null int64 
    # HelpfulnessDenominator    5 non-null int64 
    # Score                     5 non-null int64 
    # Time                      5 non-null int64 
    # Summary                   5 non-null object 
    # Text                      5 non-null object 
    # dtypes: int64(5), object(5) 



# Summary баганын эхний 5 утгыг харах
df.Summary.head(5)

# Гаралт:
    # 0    Good Quality Dog Food 
    # 1        Not as Advertised
    # 2    “Delight” says it all 
    # 3           Cough Medicine 
    # 4              Great taffy
# dtype: object



# Text буюу дэлгэрэнгүй тайлбарыг харах
df.Text.head(5)

# Гаралт:
    # 0    I have bought several of the Vitality canned d... 
    # 1    Product arrived labeled as Jumbo Salted Peanut... 
    # 2    This is a confection that has been around a fe... 
    # 3    If you are looking for the secret ingredient i... 
    # 4    Great taffy at a great price.  There was a wid...



# Текстийг урьдчилан бэлтгэхэд шаардлагатай сангууд
from nltk.corpus import stopwords	
from textblob import TextBlob, Word

# ‘Text’ баганын бүх үгийг жижиг үсэг рүү хөрвүүлэх
df['Text'] = df['Text'].apply(lambda x: " ".join(x.lower() for x in x.split()))

# Текстээс цэг, таслал зэрэг цэвэрлэх (тусгай тэмдэгтийг арилгах)
df['Text'] = df['Text'].str.replace('[^\w\s]', '')

# Цэвэрлэсэн ‘Text’ баганын эхний 5 мөрийг харах
df.Text.head(5) 

# Гаралт: 
    # 0    i have bought several of the vitality canned d... 
    # 1    product arrived labeled as jumbo salted peanut... 
    # 2    this is a confection that has been around a fe... 
    # 3    if you are looking for the secret ingredient i... 
    # 4    great taffy at a great price there was a wide ...



# Зогсоох үгсийг арилгах
stop = stopwords.words('english')

# 'Text' баганын өгөгдлөөс зогсоох үгсийг устгах
df['Text'] = df['Text'].apply(lambda x: " ".join(x for x in x.split() if x not in stop))

df.Text.head(4) 
# Гаралт: 
    # 0    bought several vitality canned dog food produc... 
    # 1    product arrived labeled jumbo salted peanutsth... 
    # 2    confection around centuries light pillowy citr... 
    # 3    looking secret ingredient robitussin believe f... 




# Зөв бичгийн алдаа шалгах
df['Text'] = df['Text'].apply(lambda x: str(TextBlob(x).correct()))

df.Text.head(5) 
# Гаралт: 
    # 0    bought several vitality canned dog food produc... 
    # 1    product arrived labelled lumbo halted peanutst... 
    # 2    connection around centuries light pillow citie... 
    # 3    looking secret ingredient robitussin believe f... 
    # 4    great staff great price wide assortment mummy ...





min_count = 29743  # хамгийн бага сэтгэгдлийн тоо

score_1 = reviews[reviews['Score'] == 1].sample(n=min_count)
score_2 = reviews[reviews['Score'] == 2].sample(n=min_count)
score_3 = reviews[reviews['Score'] == 3].sample(n=min_count)
score_4 = reviews[reviews['Score'] == 4].sample(n=min_count)
score_5 = reviews[reviews['Score'] == 5].sample(n=min_count)

# Тэнцвэртэй өгөгдлийг нэгтгэх
reviews_sample = pd.concat([score_1, score_2, score_3, score_4, score_5], axis=0)

# Индексыг дахин дэс дарааллаар шинээр үүсгэх 
reviews_sample.reset_index(drop=True, inplace=True)





# Score баганын үнэлгээ тус бүрийн давтамжийг шалгах
print(reviews_sample.groupby('Score').count().Id)

# Гаралт:
    # Score 
    # 1    29743 
    # 2    29743 
    # 3    29743 
    # 4    29743 
    # 5    29743



# Summary баганын үгсээр үгэн үүл (Word Cloud) үүсгэх
from wordcloud import WordCloud
from wordcloud import STOPWORDS

# Wordcloud функцийн оролт нь дан тэмдэгт мөр байх шаардлагатай.
# Тиймээс энд бүх текстийг залгаж нэг тэмдэгт мөр болгоно.
# Үүнтэй адил Text баганыг нэгтгэх боломжтой.
reviews_str = reviews_sample.Summary.str.cat()

# # Үгэн үүл үүсгэх объект
wordcloud = WordCloud(background_color='white').generate(reviews_str)

# Үгэн үүлийг зурж харуулах
plt.figure(figsize=(10, 10))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")  # Тэнхлэгийг нуух
plt.title('Summary баганын үгсийн үгэн үүл')
plt.show()




# өгөгдлийг Negative (оноо 1-2) болон Positive (оноо 4-5) гэж хуваах
negative_reviews = reviews_sample[reviews_sample['Score'].isin([1,2]) ]
positive_reviews = reviews_sample[reviews_sample['Score'].isin([4,5]) ]

# Тус бүрийн Summary-г нэг мөр болгон нийлүүлэх
negative_reviews_str = negative_reviews.Summary.str.cat()
positive_reviews_str = positive_reviews.Summary.str.cat()

# Negative үнэлгээний үгсийн үгэн үүл үүсгэх
wordcloud_negative = WordCloud(background_color='white').generate(negative_reviews_str)

# Positive үнэлгээний үгсийн үгэн үүл үүсгэх
wordcloud_positive = WordCloud(background_color='white').generate(positive_reviews_str)




# Сөрөг үнэлгээтэй санал хүсэлтийн үгэн үүл зурж харуулах
fig = plt.figure(figsize=(10, 10)) # графикийн хэмжээ
ax1 = fig.add_subplot(211)
ax1.imshow(wordcloud_negative, interpolation='bilinear')
ax1.axis("off")
ax1.set_title('Сөрөг үнэлгээтэй санал хүсэлтүүд', fontsize=20)




# Эерэг үнэлгээтэй санал хүсэлтийн үгэн үүл зурж харуулах
ax2 = fig.add_subplot(212)
ax2.imshow(wordcloud_positive, interpolation='bilinear')
ax2.axis("off")
ax2.set_title('Эерэг үнэлгээтэй санал хүсэлтүүд', fontsize=20)

# Графикуудыг харуулах
plt.show()




# Шаардлагатай сангуудыг импортлох
import pandas as pd        # Өгөгдөл боловсруулах
import numpy as np         # Тооцоолол хийх
import matplotlib.pyplot as plt  # График зураг гаргах
import seaborn as sns      # График загварчлахад туслах
import re                  # Текст боловсруулах (регуляр илэрхийлэл)
import os                  # Файлын системтэй ажиллах
import sys                 # Системийн түвшний команд удирдах
import ast                 # Текстийг Python объект болгон хөрвүүлэх

# График харуулах тохиргоо
%matplotlib inline
plt.style.use('fivethirtyeight')  # Графикийн загвар тохируулах




# VADER сэтгэгдлийн шинжилгээ хийх модуль
!pip install vaderSentiment
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer 
# Өнгөний палитр авах (зураг, графикт өнгө тохируулахад ашиглана)
cp = sns.color_palette()
# VADER сэтгэгдлийн шинжилгээ хийх объектыг үүсгэж байна
analyzer = SentimentIntensityAnalyzer()




# Датафреймийн 'Text' баганын бүх өгүүлбэрт сэтгэгдлийн хандлагыг тодорхойлох
# Хандлагын үр дүнг хадгалах хоосон жагсаалт
emptyline=[]
for row in df['Text']: 
        # Тухайн өгүүлбэрийн сэтгэгдлийн оноог тооцох
    vs=analyzer.polarity_scores(row)
    emptyline.append(vs)




# Хандлагын шинжилгээний үр дүнг датафрейм болгон хувиргах
df_sentiments=pd.DataFrame(emptyline)
# Эхний 5 мөрийг харах
df_sentiments.head(5)

# Гаралт:
    #     compound    neg     neu     pos 
    # 0     0.9413    0.000   0.503   0.497 
    # 1    -0.5719    0.258   0.644   0.099 
    # 2     0.8031    0.133   0.599   0.268 
    # 3     0.4404    0.000   0.854   0.146 
    # 4     0.9186    0.000   0.455   0.545





# Санал хүсэлтийн өгөгдөл болон хандлагын оноог нэгтгэх
df_c = pd.concat([df.reset_index(drop=True), df_sentiments], axis=1)
# Эхний 3 мөрийг харах
df_c.head(3)



# Compound оноог эерэг болон сөрөг хандлага руу ангилах
df_c['Sentiment'] = np.where(df_c['compound'] >= 0 , 'Positive', 'Negative')
# Эхний 5 мөрийг харах
df_c.head(5)




# Эерэг болон сөрөг хандлагын тоог тоолох
result=df_c['Sentiment'].value_counts()
# Хандлагын тоог баганан графикаар харуулах
result.plot(kind='bar', rot=0, color=['b', 'r']);


# Бүтээгдэхүүн тус бүрийн хандлагын тоог тоолох
result=df_c.groupby('ProductId')['Sentiment'].value_counts().unstack() 
# Сөрөг ба эерэг хандлагын тоог баганан графикаар дүрслэх
result[['Negative', 'Positive']].plot(kind='bar', rot=0, color='rb')
