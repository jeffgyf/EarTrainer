import pygame
import time
import random
from functools import reduce
import numpy as np
import os
pitch_names=["do","re","mi","fa","so","la","si"]

REPEAT_TIME=100
PITCH_NUM=3

def clear_console():
    if os.name=='nt':
        os.system("cls")
    else:
        os.system("clear")

def play(filename):
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        None

if __name__=="__main__":
    pygame.mixer.init()
    random.seed(time.ctime())
    for i in range(REPEAT_TIME):
        clear_console()
        pitches=[np.random.randint(0,7) for k in range(PITCH_NUM)]
        print(reduce((lambda s,i: s+i+" "), map(lambda e: pitch_names[e], pitches), ""))
        time.sleep(0.5)
        list(map((lambda e: play(str(e+1)+".wav")), pitches))
        time.sleep(1)
        


