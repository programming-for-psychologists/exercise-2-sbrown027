#M ake the program randomly alternate between first names and last names.

import time
import sys
import random
from psychopy import visual,event,core,gui


names = open('names.txt', 'r').readlines()
firstNames = [name.split(' ')[0] for name in names]
lastNames = [name.split(' ')[1] for name in names]
"""
the two line above are a more compact way of writing: 
names = open('names.txt', 'r').readlines()
firstNames=[]
for name in names:
    firstNames.append(name.split(' ')[0])
"""	

win = visual.Window([800,600],color="black", units='pix')
nameStim = visual.TextStim(win,text="", height=40, color="white",pos=[0,0])
showFirstName = True
while True:
    if showFirstName == True:
    	nameShown = random.choice(firstNames)
    else:
    	nameShown = random.choice(lastNames)
    nameStim.setText(nameShown)
    nameStim.draw()
    win.flip()
    core.wait(.75)
    win.flip()
    core.wait(.15)
    showFirstName = not showFirstName
    if event.getKeys(['q']):
        break