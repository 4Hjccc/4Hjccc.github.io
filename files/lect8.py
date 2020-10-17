# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 16:51:46 2019

@author: work
"""


import tkinter 

# create a GUI window 
root = tkinter.Tk() 

# set the title 
root.title("Label Example") 

# set the size 
root.geometry("400x200") 


# add an instructions label 
label = tkinter.Label(root, text = "Hellow World!") 								
label.pack() 

# start the GUI 
root.mainloop() 