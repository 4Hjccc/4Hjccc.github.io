# -*- coding: utf-8 -*-
"""
Created on Fri May 31 14:21:31 2019

@author: work
"""

for x in range(5):
    print("x=", str(x))
    
print()
    
x=0    
while x<5:
    print("x=", x)
    x=x+1
    
print()
    
for x in range(1, 10):
    line = ""
    for y in range(1, x+1):
        line = line + str(x)+"X"+str(y)+"="+str(x*y)+" "
    print(line)
    
# guessing game
    
import random
num = random.randint(1, 15)
cnt=1
correct = False

while((not correct) and cnt<=4 ):
    guess = input("Enter your number (1-15): ")
    guess_num = int(guess)
    if (guess_num>num):
        print("Your guess is too large")
    elif (guess_num<num):
        print("Your guess is too small")
    else:
        print("Your guess is correct!")
        correct = True
    cnt = cnt+1

if (correct):
    print("You win the game")
else:
    print("You lose the game. The number is", num)

# break the loop
for k in range(10):
    if k==5:
        break
    print(k)
            
