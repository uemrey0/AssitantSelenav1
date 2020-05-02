import speech_recognition as sr
import time
from Commands import Command
from playsound import playsound
print('Merhaba Emre ben senin kişisel asistanın Selena.')
playsound('welcome.mp3')
r = sr.Recognizer()
while True:
    with sr.Microphone() as source:
         print ("Seni Dinliyorum...")
         playsound('senidinliyorum.mp3')
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
