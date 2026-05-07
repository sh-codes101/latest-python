import random
from gtts import gTTS
import os

lines = [
    '''HI SHOURYA BOSS.
    SO WHAT ARE PLANS TODAY
    I AM YOUR PERSONAL ASSISTANT 
           YOUR PC
    ''',
]

text = random.choice(lines)

tts = gTTS(text=text, lang='hi')
tts.save("fun.mp3")

os.system("start fun.mp3")