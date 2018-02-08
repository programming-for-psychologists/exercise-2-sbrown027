# Pop up a box that accepts a first name, and check to make sure that the name exists. If it doesn't, pop-up a 'Name does not exist'error box

# userVar = {'Name':'Enter your name'}
# dlg = gui.DlgFromDict(userVar)
import time
import sys
import random
from psychopy import visual,event,core,gui

userVar = {'Name' : 'Enter your name'}
dlg = gui.DlgFromDict(userVar)

names = open('names.txt', 'r').readlines()

if userVar['Name'] not in names:

	def popupError(text):
		errorDlg = gui.Dlg(title="Error", pos=(200,400))
		errorDlg.addText('Error: '+text, color='Red')
		errorDlg.show()
	popupError('Name Does not exist!')