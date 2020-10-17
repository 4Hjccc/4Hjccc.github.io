# -*- coding: utf-8 -*-
"""
Created on Fri May 31 11:02:33 2019

@author: work
"""

a=10;
b=22;
if (a>b):
    print ("a is larger than b")
    print("The larger value is", a)
else:
    print("a is not larger than b")
    print("The larger value is", b)
    
print("The comparison is compelet")

a=10
b=10
if (a>b):
    print ("a is larger than b")
    print("The larger value is", a)
elif (a==b):
    print("a and b have the same value")
else:
    print("a is not larger than b")
    print("The larger value is", b)   
    
a=10
b=11
if (a>b):
    print ("a is larger than b")
    print("The larger value is", a)
    
a=10
if (a<5):
    print("a is smaller than 5")
elif (a>100):
    print("a is larger than 100")
elif(a>80):
    print("a is larger than 8")
    
a=10
b=12
if (a>0 and b>0):
    print("Both a and b are postive numbers")
    
if (a>0 or b>0):
    print("At least one of a and b is positive")
    
if (not a<0):
    print("a is not a negative number")
    
        
  