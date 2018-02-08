# Now, instead of waiting for a response forever, let's implement a timeout. Show accuracy feedback as before, but now also show a red 'X' if no 
# response is received for 1 sec (and go on to the next trial automatically following the feedback). (Use psychopy timers)

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
posFB = visual.TextStim(win,text="0", height=40, color="green",pos=[0,0])
negFB = visual.TextStim(win,text="X", height=40, color="red",pos=[0,0])

showFirstName = True
while True:
	if showFirstName == True:
		nameShown = random.choice(firstNames)
		nameType = 'f'
	else:
		nameShown = random.choice(lastNames)
		nameType = 'l'
	nameStim.setText(nameShown)
	nameStim.draw()
	win.flip()
	keyPressedList = event.waitKeys(keyList=['l','f'], maxWait = 1)
	win.flip()	
	if keyPressedList == None:
		negFB.draw()
	elif nameType in keyPressedList: 
		posFB.draw()
	else:
		negFB.draw()
	win.flip()
	core.wait(.5)
	win.flip()
	showFirstName = not showFirstName
	if event.getKeys(['q']):
		break