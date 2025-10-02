import json
import requests

# JSONPlaceholder API-с өгөгдөл татах
response = requests.get("https://jsonplaceholder.typicode.com/posts")

# Өгөгдлийг JSON формат руу хөрвүүлэх
data = response.json()

# Хэвлэх
print(json.dumps(data, indent = 5))

# 0 -д харъяалагдах постыг сонгох
text = data[0]
# 0 -д харъяалагдах постоос title, body-г авах
print(text['title'], '\n**', text['body'])

# 51 -д харъяалагдах постыг сонгох
text = data[51]
# 51 -д харъяалагдах постоос title, body-г авах
print(text['title'], '\n**', text['body'])
