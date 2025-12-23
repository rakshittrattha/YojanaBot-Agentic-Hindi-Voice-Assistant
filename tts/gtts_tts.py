from gtts import gTTS
from playsound import playsound
import os

def speak_hindi(text):
    try:
        tts=gTTS(text=text, lang='hi')
        file="output.mp3"
        tts.save(file)
        playsound(file)
        os.remove(file)
    except Exception as e:
        print("TTS Error:", e)
