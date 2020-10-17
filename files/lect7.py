# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 16:47:17 2019

@author: work
"""


face ="\U0001f604"    # smiling face emoji  
thumbup="\U0001f44d"    # thumb up emoji

line =""
for k in range(5):
    line += face
print(line)

print("Coding python program is interesting")

line =""
for k in range(5):
    line += face
print(line)

print("You are doing great!")

line =""
for k in range(5):
    line += thumbup
print(line)

print()

face ="\U0001f604"    # smiling face emoji  
thumbup="\U0001f44d"    # thumb up emoji

def printSmilingFace():
    line =""
    for k in range(5):
        line += face
    print(line)


def printThumbup():
    line =""
    for k in range(5):
        line += thumbup
    print(line)
    
printSmilingFace()
print("Coding python program is interesting")
printSmilingFace()
print("You are doing great!")
printThumbup()

print()

face ="\U0001f604"    # smiling face emoji  
thumbup="\U0001f44d"    # thumb up emoji

def printEmoji(emoji, num):
    line =""
    for k in range(num):
        line += emoji
    print(line)
    
printEmoji(face, 5)
print("Coding python program is interesting")
printEmoji(face, 8)
print("You are doing great!")
printEmoji(thumbup, 9)

print()

import random
face ="\U0001f604"    # smiling face emoji  
thumbup="\U0001f44d"    # thumb up emoji

def printEmoji(emoji):
    line =""
    num = random.randint(1, 8)
    for k in range(num):
        line += emoji
    print(line)
    return num
    
a = printEmoji(face)
print("Coding python program is interesting")
b = printEmoji(face)
print("You are doing great!")
c = printEmoji(thumbup)
print("Number of Emojis printed is:", a+b+c)