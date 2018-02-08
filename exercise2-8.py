# Extend the task by requiring the subject to respond by pressing a spacebar (the key is called 'space'), 
# as quickly as possible anytime the name on the screen matches the name you entered into the box 
# (so if I enter 'Gary' I would have to press 'space' anytime the name 'Gary' shows up. 
# If the participant presses 'space' to the wrong name (false alarm), or misses the name (a miss), show a red X.


import time
import sys
import random
from psychopy import visual,event,core,gui

userVar = {'Name' : 'Enter your name'}
dlg = gui.DlgFromDict(userVar)

names = open('names.txt', 'r').readlines()
firstNames = [name.split(' ')[0] for name in names]
lastNames = [name.split(' ')[1] for name in names]


if userVar['Name'] not in firstNames:

	def popupError(text):
		errorDlg = gui.Dlg(title="Error", pos=(200,400))
		errorDlg.addText('Error: '+text, color='Red')
		errorDlg.show()
	popupError('Name Does not exist!')


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
	spaceKey = event.waitKeys(keyList=['space'], maxWait=1)
	if nameShown == userVar['Name']:
		if spaceKey == None:
			negFB.draw()
			win.flip()
			core.wait(.5)

	win.flip()
	core.wait(.5)
	win.flip()
	showFirstName = not showFirstName
	if event.getKeys(['q']):
		break