# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 20:13:34 2019

@author: work
"""
import random
from time import *

word_tuple = ("program", "computer", "club", "software", "hardware", "circuit",
              "mall", "movie", "television", "theater", "shopping", "hotel",
              "diplomatic", "etiquette", "candidate", "support", "require", "demand",
              "edge", "voice", "vision", "content", "camera", "process",
              "wildspread", "public", "awareness", "system", "autonomous", "enable",
              "fanbase", "mind", "mindset", "wish", "hope", "will")

init_num = 5
words = []
tstep = 3.0
tdiff = 0.0

#create the initial word list
for k in range(init_num):
    num = random.randint(0, 35)
    words.append(word_tuple[num])

word_num = len(words)

while word_num>0 and word_num<10:
    new_word_num = int(tdiff/tstep)
    for k in range(new_word_num):
        words.append(word_tuple[random.randint(0, 35)])
        
    #print the word list
    line=""
    for w in words:
        line = line + w +" " 
    print(line)

    # start the timer
    start_time = time()
    inword=input("Type:")
    
    # check if the typed word is in the words list
    # you will write your program here
    
    # stop the timer
    end_time = time()
    tdiff=end_time-start_time
            
# check game results
if word_num==0:
    print("You win the game")
else:
    print("You lose the game")
        