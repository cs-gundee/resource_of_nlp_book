# tweepy суулгах
!pip install tweepy

# Шаардлагатай сангуудыг импортлох
import tweepy, os

# Google colab орчны хувьсагчийг унших объект
from google.colab import userdata

# Bearer token ашиглан client объект үүсгэх
client = tweepy.Client(bearer_token = userdata.get('BEARER_TOKEN'))

# Жиргээг хайж татах хүсэлт илгээх
response = client.search_recent_tweets(
    # 'dell' үгтэй, retweet биш, англи хэл дээрх жиргээ
	  query = "dell -is:retweet lang:en", 
    # Дээд тал нь 10 жиргээ авах
    max_results=10,  
    # Нэмэлт талбарууд авах
	  tweet_fields = ["author_id", "created_at", "lang"]  
)

# Татсан жиргээнүүдийг хэвлэх
for t in response.data:
    print(t.id, t.text)
