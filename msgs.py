import random
import pyautogui as  pg
import time
animal=('1','2','3')
time.sleep(2)
for i in range(10):
    a=random.choice(animal)
    pg.write("You are my " + a)

    pg.press('enter')

