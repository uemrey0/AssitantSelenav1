import speech_recognition as sr
import time
from Commands import Command
from playsound import playsound
from gtts import gTTS
r = sr.Recognizer
#Merhaba mesajı
def welcome_msg(text):
    fileName = "welcome.mp3"
    tts = gTTS(text=text, lang="tr")
    tts.save(fileName)
    print(text)
    playsound(fileName)
    os.remove(fileName)
    
    
print("Asistan'a Hoşgeldiniz.")
playsound("welcome_msg.mp3")
user= input("Adınızı Giriniz:")
welcomeMSG = "Merhaba {} Asistan'a Hoşgeldin. Ben senin kişisel asistanın Selena".format(user)
welcome_msg(welcomeMSG)



#Döngü
while True:
    with sr.Microphone() as source:
         iamlistenning="Seni diliyorum {}".format(user)
         print(iamlistenning)
         talk(iamlistenning)
         audio = r.listen(source)

    data = ""
    try:
        data = r.recognize_google(audio, language='tr')
        print(data)
        command = Command(data)
        command.findCommand()
        time.sleep(1)

    except sr.UnknownValueError:
        print("Ne dediğini anlamadım dostum:(")
        playsound('error.mp3')
