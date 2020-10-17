# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 09:02:33 2019

@author: work
"""
numlist=[1, 7, 9, 9]
print(numlist)
print(numlist[3])
fruitlist=["apple", "grape", "pear"]
print(fruitlist)
print(fruitlist[1])

print("")

numlist=[1,12, 9, 9, 6, 9]
print("Number of 9 in the list is:\t", numlist.count(9))
print("The first position of 9 is:\t", numlist.index(9))
numlist.sort()
print("Sorted list is:\t\t\t", numlist)
numlist.reverse()
print("Reverse sorted list is\t\t", numlist)

print("")

fruitlist=["apple", "grape", "pear"]
vegalist=["lattuce", "carrot"]
fruitlist.append("peach")
print("The new list is:\t", fruitlist)
fruitlist.remove("grape")
print("After remove grage:\t", fruitlist)
tbe = fruitlist.pop(2)
print("Removed from the list:\t", tbe)
print("The new list is:\t", fruitlist)
fruitlist.extend(vegalist)
print("The extened list is:\t", fruitlist)

print("")

fruitlist=["apple", "grape", "pear"]
fruitlist[1]="peach"

for x in range(len(fruitlist)):
    print(fruitlist[x])

for x in fruitlist:
    print(x)
    
fruit_tuple=("apple", "grape", "pear")
print(fruit_tuple)
print(fruit_tuple[1])
print(len(fruit_tuple))