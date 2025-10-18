# ------------------------------
# Суурь сангууд
# ------------------------------
import os
import string
from io import StringIO

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ------------------------------
# NLP (Natural Language Processing)
# ------------------------------
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer, PorterStemmer
from textblob import TextBlob, Word

# ------------------------------
# Scikit-learn: онцлог шинж боловсруулах
# ------------------------------
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

# ------------------------------
# Scikit-learn: өгөгдөл хуваах, урьдчилан боловсруулах
# ------------------------------
from sklearn import model_selection, preprocessing, metrics
from sklearn.model_selection import train_test_split, cross_val_score

# ------------------------------
# Scikit-learn: загварууд
# ------------------------------ 
from sklearn import linear_model
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import LinearSVC



# Татаж авсан өгөгдлийг унших
Data = pd.read_csv('consumer_complaints.csv', encoding='latin-1')

# Баганын нэрсийг харах
print(Data.dtypes)



# Шаардлагатай багануудыг сонгох
Data = Data[['product', 'consumer_complaint_narrative']]

# 'consumer_complaint_narrative' баганын утга хоосон биш (null биш) мөрүүдийг хадгалах
Data = Data[pd.notnull(Data['consumer_complaint_narrative'])]

# Эхний 5 мөрийг хэвлэх
print(Data.head())



# 'product' баганыг тоон ангилалд хөрвүүлэх
Data['category_id'] = Data['product'].factorize()[0]

# Өгөгдлийн эхний 5 мөрийг хэвлэх
print(Data.head())



# Гомдлын ангилал тус бүрт ногдох гомдлын тоог тоолох
Data.groupby('product').consumer_complaint_narrative.count()



# График дүрслэл үүсгэх
fig = plt.figure(figsize=(8,6))
Data.groupby('product').consumer_complaint_narrative.count().plot.bar(ylim=0)
plt.show()



# Өгөгдлийг хуваах
train_x, valid_x, train_y, valid_y = model_selection.train_test_split(Data['consumer_complaint_narrative'], Data['product'])



# LabelEncoder-ээр ангиллын шошгыг тоон код руу хөрвүүлэх
encoder = preprocessing.LabelEncoder()

# Сургалтын шошго дээр fit, transform хийх
train_y = encoder.fit_transform(train_y) 

# Үнэлгээний шошго дээр fit, transform хийх
valid_y = encoder.fit_transform(valid_y)

# TF-IDF векторизатор үүсгэх
tfidf_vect = TfidfVectorizer(analyzer='word', token_pattern=r'\w{1,}', max_features=5000)

# Бүх өгөгдлийн текст дээр fit хийх
tfidf_vect.fit(Data['consumer_complaint_narrative'])

# Сургалтын болон үнэлгээний текст өгөгдлийг TF-IDF-д хөрвүүлэх
xtrain_tfidf =  tfidf_vect.transform(train_x)
xvalid_tfidf =  tfidf_vect.transform(valid_x)



# Логистик регрессийн загвар үүсгэж, сургалтын өгөгдөл дээр сургах
model = linear_model.LogisticRegression().fit(xtrain_tfidf, train_y)

# загварын нэгтгэл
LogisticRegression(
    C = 1.0,                  # Регуляцийн коэффициент 
    class_weight = None,      # Ангиллын жинг тохируулах
    dual = False,             # Дуугаар тооцох эсэх
    fit_intercept = True,     # Интерсепт (байгуулагч) тооцох эсэх
    intercept_scaling = 1,    # Интерсептийн масштаб
    max_iter = 100,           # Итгэх түвшинд хүрэх хүртэлх давталтын тоо
    multi_class = 'ovr',      # Олон ангиллын аргын төрөл (“one-vs-rest”)
    n_jobs = 1,               # Олон CPU ашиглах эсэх
    penalty = 'l2',           # Регуляцийн төрөл (L2-регуляци)
    random_state = None,      # Санамсаргүй тооны эхлэл
    solver = 'liblinear',     # Оновчлох арга
    tol = 0.0001,             # Зохиомол зөрүүний зөвшөөрөгдөх хэмжээ
    verbose = 0,              # Илүү дэлгэрэнгүй мэдээлэл үзүүлэх эсэх
    warm_start = False        # Загварыг дахин ашиглах эсэх
)



# Үнэлгээний өгөгдлийн таамаглал гаргаж авах
predictions = model.predict(xvalid_tfidf)

# Нарийвчлал тооцох
accuracy = metrics.accuracy_score(valid_y, predictions)

# Үр дүн хэвлэх
print ("Accuracy: ", accuracy)
# Гаралт:
    # Accuracy:  0.845048497186 



# Ангиллын гүйцэтгэлийн тайлан хэвлэх
print(metrics.classification_report(
    valid_y, 
    model.predict(xvalid_tfidf),
    target_names=Data['product'].unique()
))



# Confusion матриц үүсгэх
conf_mat = confusion_matrix(valid_y, model.predict(xvalid_tfidf))

# Ангиллын ID ба нэрийг холбосон датафрейм үүсгэх
category_id_df = Data[['product', 'category_id']].drop_duplicates().sort_values('category_id')

# Ангиллын нэрсийг axis-д үзүүлэхэд ашиглахын тулд жагсаалт гаргаж авах
category_to_id = dict(category_id_df.values)
id_to_category = dict(category_id_df[['category_id', 'product']].values)


# График үүсгэх, confusion matrix-г дулаан зураг хэлбэрээр дүрслэх
fig, ax = plt.subplots(figsize=(8,6))
sns.heatmap(conf_mat, annot=True, fmt='d', cmap="BuPu",
            xticklabels=category_id_df[['product']].values, yticklabels=category_id_df[['product']].values)
plt.ylabel('Жинхэнэ ангилал')
plt.xlabel('Таамагласан ангилал') 
plt.title('Confusion матриц')
plt.show()





# Таамаглах текст
texts = ["This company refuses to provide me verification and validation of debt per my right under the FDCPA. I do not believe this debt is mine."]

# Шинэ текстийг TF-IDF формат руу хөрвүүлэх
text_features = tfidf_vect.transform(texts)

# Хөрвүүлсэн өгөгдөл дээр таамаглах
predictions = model.predict(text_features)




# Текстийг хэвлэх
print(texts)
# Таамагласан ангиллыг хэвлэх
print("Таамагласан ангилал: '{}'".format(id_to_category[predictions[0]]))
