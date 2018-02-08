# Now let's implement some feedback. Let's allow either a 'f' or 'l' response for each trial. If the response is correct, show a green 'O' before 
# the start of the next trial. If the response is wrong, show a red 'X' (you can use textStim objects for feedback). Show the feedback for 500 ms.  # Note: we have someone in a class whose last name is a common first name. If this were an experiment, how might this affect responses?


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
	keyPressedList = event.waitKeys(keyList=['l','f'])
	win.flip()	
	if nameType in keyPressedList: 
		posFB.draw()
	else:
		negFB.draw()
	win.flip()
	core.wait(.5)
	win.flip()
	showFirstName = not showFirstName
	if event.getKeys(['q']):
		break
