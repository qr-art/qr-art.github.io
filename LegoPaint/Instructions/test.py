from gtts import gTTS
from playsound import playsound
import time
import os
import urllib.request
import sys


def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host) #Python 3.x
        return True
    except:
        return False

### Read File with instructions

# python instruction.csv 1

if not connect():
    raise Exception("No Internet Connection!")

# path_to_file = 'instruction.csv'
# speed = 1

path_to_file = sys.argv[0]
speed = sys.argv[1] #seconds

with open(path_to_file) as f:
    contents = f.readlines()

row = 1

for inst in contents:
    row = row + 1
    values = inst.split(',')
    for column, color_code in enumerate(values, 1):
        tts = gTTS( color_code, lang= "it")
        file_path = "instruction.mp3"

        tts.save(file_path)
        playsound(file_path)
        os.remove(file_path)

        print(f'row: {row} - column: {column} - {color_code}')
        time.sleep(speed)


