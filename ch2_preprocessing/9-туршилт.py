tweet_sample= "How to take control of your #debt https://medium.com/change-your-mind/a-guide-to-family-finance-strategies-732a5369d529.#Best advice for #family #financial #success (@MashaRusanov)"

def processRow(row):
    import re
    import nltk
    nltk.download('wordnet')
    from textblob import TextBlob
    from nltk.corpus import stopwords
    from nltk.stem import PorterStemmer
    from textblob import Word
    from nltk.util import ngrams
    import re
    from wordcloud import WordCloud, STOPWORDS
    from nltk.tokenize import word_tokenize

    tweet = row
    # үсгийг жижигрүүлэх
    tweet.lower()
    # "\u002c", "x96" гэх мэт юникод тэмдэгтийг устгах
    tweet = re.sub(r'(\\u[0-9A-Fa-f]+)', r'', tweet)
    tweet = re.sub(r'[^\x00-\x7f]', r'', tweet)
    # ямар ч url -г URL руу хувиргах
    tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))','URL', tweet)
    # ямар ч @Username -г "AT_USER" болгох
    tweet = re.sub('@[^\s]+','AT_USER', tweet)
    # илүү хоосон зайг устгах
    tweet = re.sub('[\s]+', ' ', tweet)
    tweet = re.sub('[\n]+', ' ', tweet)
    # үсэг, тоо бус тэмдэгтүүдийн хоосон зайг хасах
    tweet = re.sub(r'[^\w]', ' ', tweet)
    # үгийн урд байрлах хашилтыг устгах """
    tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
    # # тэмдэгттэй үгийг дан үг болгох
    tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
    # :( болон :) тэмдэгт мөрийг устгах
    tweet = tweet.replace(':)','')
    tweet = tweet.replace(':(','')
    # тоог арилгах
    tweet = ''.join([i for i in tweet if not i.isdigit()])
    # анхаарлын тэмдэг устгах
    tweet = re.sub(r"(\!)\1+", ' ', tweet)
    # асуултын тэмдэг устгах
    tweet = re.sub(r"(\?)\1+", ' ', tweet)
    # цэг устгах
    tweet = re.sub(r"(\.)\1+", ' ', tweet)
    # лемма
    from textblob import Word
    tweet =" ".join([Word(word).lemmatize() for word in tweet.split()])
    # язгуур олох
    # st = PorterStemmer()
    # tweet=" ".join([st.stem(word) for word in tweet.split()])
        # Эможи устгах
    tweet = re.sub(':\)|;\)|:-\)|\(-:|:-D|=D|:P|xD|X-p|\^\^|:-*|\^\.\^|\^\-\^|\^\_\^|\,-\)|\)-:|:\'\(|:\(|:-\(|:\S|T\.T|\.\_\.|:<|:-\S|:-<|\*\-\*|:O|=O|=\-O|O\.o|XO|O\_O|:-\@|=/|:/|X\-\(|>\.<|>=\(|D:', '', tweet)
    # тэгшлэх
    tweet = tweet.strip('\'"')
    row = tweet
    return row

# функцийг дуудаж ажиллуулах
processRow(tweet_sample)

# Гаралт:
# 'How to take control of your debt URL Best advice for family financial success AT_USER'

