# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

print("Hello World")
print(1+2+3)

name = input("what is your name? ")
print("Hello",  name)

# perform multiplication for you
print("This program will perform multiplication x*y")
x = float(input("PLease type x vale: "))
y = float(input("Please type y: "))
print("The product of x and y is:")
print(x*y)

import datetime
date_time = datetime.datetime.now()
date = date_time.date()  # Gives the date
time = date_time.time()  # Gives the time
print("Today is (Year Month Day):")
print(date.year, date.month, date.day)
print("The current time is (Hour Minute Second):" )
print(time.hour, time.minute, time.second)