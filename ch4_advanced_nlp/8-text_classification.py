import pandas as pd

# Өгөгдлийг "spam.csv" файлаас унших. 
# encoding='latin1' текстийн кодлолоор латин1-г ашиглаж байгааг заана.
Email_Data = pd.read_csv("spam.csv", encoding='latin1')

# Өгөгдлийн багануудын нэрсийг шалгах
print(Email_Data.columns)
# Гаралт:
# Index(['v1', 'v2', 'Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4'], dtype= 'object')

#  Зөвхөн хэрэгтэй баганууд болох 'v1' ба 'v2'-г сонгож авах
Email_Data = Email_Data[['v1', 'v2']]

# Баганын нэрсийг ойлгомжтой болгох зорилгоор "v1" -> "Target"
# "v2" -> "Email" (имэйл мессеж) гэж өөрчлөх
Email_Data = Email_Data.rename(columns={"v1": "Target", "v2": "Email"})

# Өгөгдлийн эхний хэдэн мөрийг харуулах
Email_Data.head()

# Гаралт:
    # Target   Email 
    # 0      ham   Go until jurong point, crazy.. Available only ... 
    # 1      ham   Ok lar... Joking wif u oni... 
    # 2      spam  Free entry in 2 a wkly comp to win FA Cup fina... 
    # 3      ham   U dun say so early hor... U c already then say... 
    # 4      ham   Nah I don't think he goes to usf, he lives aro...


# Ерөнхий зориулалтын сангууд
import string
import pandas as pd

# Текст боловсруулах сангууд
import nltk
nltk.download('stopwords')
nltk.download('wordnet')
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from textblob import Word


# Бүх текстийг жижиг үсгээр хөрвүүлэх
Email_Data['Email'] = Email_Data['Email'].apply(lambda x: " ".join(x.lower() for x in x.split()))

# Англи хэлний stopwords буюу ач холбогдол багатай үгсийн жагсаалтыг авах
stop = stopwords.words('english')

# Stopwords үгсийг текстээс устгах
Email_Data['Email'] = Email_Data['Email'].apply(lambda x: " ".join(x for x in x.split() if x not in stop))

# Үгсийн үндсийг олох зорилгоор PorterStemmer ашиглах
st = PorterStemmer()
Email_Data['Email'] = Email_Data['Email'].apply(lambda x: " ".join([st.stem(word) for word in x.split()]))

# Үгсийг зөв дүрмийн хэлбэрт (лемматизаци) оруулах
Email_Data['Email'] = Email_Data['Email'].apply(lambda x: " ".join([Word(word).lemmatize() for word in x.split()]))

# Өгөгдлийн эхний хэдэн мөрийг харуулах
Email_Data.head()

# Гаралт:
    #   Target                                              Email 
    #   0    ham  go jurong point, crazy.. avail bugi n great wo... 
    #   1    ham                        ok lar... joke wif u oni... 
    #   2    spam free entri 2 wkli comp win fa cup final tkt 21... 
    #   3    ham          u dun say earli hor... u c alreadi say... 
    #   4    ham              nah think goe usf, live around though



from sklearn import model_selection
from sklearn import preprocessing
from sklearn.feature_extraction.text import TfidfVectorizer

# Өгөгдлийг сургалтын болон баталгаажуулах (validation) хэсэгт хуваах
# train_test_split функцээр Email баганын текстийг (features) ба Target баганын шошгыг (labels) тусад нь хуваана
train_x, valid_x, train_y, valid_y = model_selection.train_test_split(Email_Data['Email'], Email_Data['Target'])

# Шошго буюу ангиллын утгуудыг тоон утгад хөрвүүлэхийн тулд LabelEncoder ашиглана
encoder = preprocessing.LabelEncoder()
train_y = encoder.fit_transform(train_y)  # Сургалтын шошгуудыг хөрвүүлэх
valid_y = encoder.fit_transform(valid_y)  # Баталгаажуулах шошгуудыг хөрвүүлэх

# TF-IDF вектор үүсгэх
# Үүнд үгсийг нэгээс дээш тэмдэгттэй гэж үзэн хамгийн ихдээ 5000 онцлог (feature) авч байна
tfidf_vect = TfidfVectorizer(analyzer='word', token_pattern=r'\w{1,}', max_features=5000)

# Бүх Email өгөгдлийг ашиглан TF-IDF векторыг сургана
tfidf_vect.fit(Email_Data['Email'])

# Сургалтын ба баталгаажуулах өгөгдлийг TF-IDF вектор болгон хувиргана
xtrain_tfidf = tfidf_vect.transform(train_x)
xvalid_tfidf = tfidf_vect.transform(valid_x)

# Сургалтын TF-IDF өгөгдлийн бүрэн бүтэц буюу өгөгдлийн матрицын дата хэсгийг шалгах
xtrain_tfidf.data

# Гаралт:
# array([0.39933971, 0.36719906, 0.60411187, ..., 0.36682939, 0.30602539, 0.38290119])


from sklearn import naive_bayes
import sklearn.metrics as metrics
from sklearn.metrics import accuracy_score
def train_model(classifier, feature_vector_train, label, feature_vector_valid, is_neural_net=False):
    # Сургалтын өгөгдлийг өгсөн ангилагчид тохируулах буюу сургах
    classifier.fit(feature_vector_train, label)
    # Баталгаажуулах өгөгдлийн шошгыг урьдчилан таамаглах
    predictions = classifier.predict(feature_vector_valid)
    # Урьдчилсан таамаглал болон бодит утгын үнэн зөв байдал буюу нарийвчлалыг тооцоолох
    return metrics.accuracy_score(predictions, valid_y)

# Naive Bayes ангилагч ашиглан сургалт явуулах жишээ
accuracy = train_model(naive_bayes.MultinomialNB(alpha=0.2), xtrain_tfidf, train_y, xvalid_tfidf)
print("Accuracy: ", accuracy)

# Гаралт:
# Accuracy:  0.9791816223977028



from sklearn import linear_model
# Логистик регрессор ашиглан сургалтын загварыг бэлтгэж, баталгаажуулах өгөгдөл дээр үнэлгээ хийх
accuracy = train_model(linear_model.LogisticRegression(), xtrain_tfidf, train_y, xvalid_tfidf)
print ("Accuracy: ", accuracy)

# Гаралт:
# Accuracy:  0.9626704953338119
