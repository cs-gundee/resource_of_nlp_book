# Жишээ өгөгдөл
review = "I like this phone. Screen quality and camera clarity is really good."
review2 = "This tv is not good. Bad quality, no clarity, worst experience"


# TextBlob санг импортлох
from textblob import TextBlob

# TextBlob нь хандлагыг таамаглах урьдчилан сургасан загвартай
# Загварыг ашиглан тухайн текстийн хандлагыг тодорхойлно
blob = TextBlob(review)

# Хандлагын оноо (туйлшрал болон субъектив байдлын утга)
blob.sentiment

# Гаралт:
# Sentiment(polarity=0.7, subjectivity=0.6000000000000001)


# review2 хувьсагч дахь өгөгдлийн хандлагыг тодорхойлъё
blob = TextBlob(review2)
blob.sentiment

# Гаралт:
# Sentiment(polarity=-0.6833333333333332, subjectivity=0.7555555555555555)
