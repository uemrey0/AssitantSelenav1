import urllib.request
import json
from gtts import gTTS
from playsound import playsound
from random import choice
import os
import sys
import requests
from lxml import html


class Command():

    def __init__(self, inSound):
        self.sound = inSound.upper()
        self.soundBlocks = self.sound.split()
        print(self.soundBlocks)
        self.commands = ["NASILSIN", "KAPAT"]

    # KONUŞMA


    def speak(self, text):
        fileName = "sound.mp3"
        tts = gTTS(text=text, lang="tr")
        tts.save(fileName)
        print(text)
        playsound(fileName)
        os.remove(fileName)

    #KOMUT İŞLEVLERİ
    def kapat(self):
        self.speak("Kapatıyorum yakışıklı sonra görüşmek üzere ;)")
        sys.exit()

    def nasılsın(self):
        naberWords = ["Benim duygularım yok ama siz insanlar sanırım bu soruya İyiyim diye cevap veriyorsunuz",
                      "Bir bilgisayar kadar mutluyum. Yo yo hayır daha fazla mutluyum.",
                      "Milyonlarca parametrem var, çok sıkıcı olduğumu söylerler genelde. ama iyiyim teşekkürler."]
        wordchoose = choice(naberWords)
        self.speak(wordchoose)

    """
    def iftar(self):
        r = requests.get ("https://www.sozcu.com.tr/imsakiye")
        tree = html.fromstring(r.content)

        iftara = tree.xpath("//*[@class=imsakiye]/div[3]/div[2]/div[1]/div[2]/ul[1]/li[5]/div[@class=day-part-time")
        self.speak(iftara)
    """
    # İŞLEVSEL
    def findCommand(self):
        for command in self.commands:
            if command in self.soundBlocks:
                self.commandRun(command)
    def commandRun(self, command):
        if command == "KAPAT":
            self.kapat()
        if command == "NASILSIN":
            self.nasılsın()
       """ 
        if command == "IFTAR":
            self.iftar()
       """

