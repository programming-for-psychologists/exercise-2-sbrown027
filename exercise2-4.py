# On each presentation of a name, wait for a response ('f' for first name, 'l' for last-name) 
# and only proceed to the next name if the response is correct. Hint: if you've done steps 2-3 properly, this should be really easy. 
# Refer to the psychopy documentation of event.waitKeys() if you have trouble.


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
    	nameType = 'f'
    else:
    	nameShown = random.choice(lastNames)
    	nameType = 'l'
    nameStim.setText(nameShown)
    nameStim.draw()
    win.flip()
    event.waitKeys(keyList=[nameType])	
    showFirstName = not showFirstName
    if event.getKeys(['q']):
        break





############

# names = open('names.txt', 'r').readlines()
# lastNames = [name.split(' ')[1] for name in names]
# firstNames = [name.split(' ')[0] for name in names]



# win = visual.Window([800,600],color="black", units='pix')
# firstNameStim = visual.TextStim(win,text="", height=40, color="white",pos=[0,0])
# lastNameStim = visual.TextStim(win,text="", height=40, color="white",pos=[0,0])
# while True:
#     nameShown = random.choice(lastNames)
#     lastNameStim.setText(nameShown)
#     lastNameStim.draw()
#     win.flip()
#     event.waitKeys(keyList=['l'])
#     if event.getKeys(['q']):
#         break
#     win.flip()
#     core.wait(.15)
#     nameShown = random.choice(firstNames)
#     firstNameStim.setText(nameShown)
#     firstNameStim.draw()
#     win.flip()
#     event.waitKeys(keyList=['f'])
#     if event.getKeys(['q']):
#         break
#     win.flip()
#     core.wait(.15)
#     if event.getKeys(['q']):
#         break