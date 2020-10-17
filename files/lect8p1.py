# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 16:51:46 2019

@author: work
"""

# import the modules 
import tkinter 
import random 

# the game time left, initially 30 seconds. 
timeleft = 30

# create a GUI window 
root = tkinter.Tk() 

# set the title 
root.title("COLORGAME") 

# set the size 
root.geometry("375x200") 


# add an instructions label 
instructions = tkinter.Label(root, text = "Type in the colour"
						"of the words, and not the word text!", 
									font = ('Helvetica', 12)) 
instructions.pack() 

# add a score label 
scoreLabel = tkinter.Label(root, text = "Press enter to start", 
									font = ('Helvetica', 12)) 
scoreLabel.pack() 

# add a time left label 
timeLabel = tkinter.Label(root, text = "Time left: " +
			str(timeleft), font = ('Helvetica', 12)) 
				
timeLabel.pack()

# add a label for displaying the colours 
label = tkinter.Label(root, font = ('Helvetica', 60)) 
label.pack() 

# add a text entry box for 
# typing in colours 
e = tkinter.Entry(root)

e.pack()
 
# start the GUI 
root.mainloop() 