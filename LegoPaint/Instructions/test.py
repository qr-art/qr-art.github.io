from gtts import gTTS
from playsound import playsound
import time
import os


### Read File with instructions

path_to_file = 'instruction.csv'
speed = 1.0 #seconds

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