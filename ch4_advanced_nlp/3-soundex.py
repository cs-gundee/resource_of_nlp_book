!pip install fuzzy
import fuzzy

# Soundex функц үүсгэх, параметр: кодын урт (4 тэмдэгт)
soundex = fuzzy.Soundex(4)

# Үгийн авиа зүйн кодыг гаргах
print(soundex('natural'))   # Гаралт: 'N364'
print(soundex('natuaral'))  # Гаралт: 'N364' (зөв бичгийн алдаатай ч адилхан код)
print(soundex('language'))  # Гаралт: 'L52'
print(soundex('processing'))# Гаралт: 'P625'
