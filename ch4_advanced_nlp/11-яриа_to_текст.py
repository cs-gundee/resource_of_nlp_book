# Сангуудыг суулгах
!pip install SpeechRecognition
!apt-get install -y portaudio19-dev
!pip install PyAudio

# Импортлох
import speech_recognition as sr



# Таних объект үүсгэх
r=sr.Recognizer()

# Микрофоноор дуу авах
with sr.Microphone() as source:
    print("Ярьж эхлээрэй:")
    audio = r.listen(source)
    print("Цаг дууслаа.")

# Авсан дууг текст болгон хөрвүүлэх    
try:
    print("Таны хэлснийг ингэж ойлголоо: " + r.recognize_google(audio));
except Exception as e:
    print("Алдаа гарлаа:", e)



