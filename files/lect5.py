# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 10:58:26 2019

@author: work
"""

x = 8
y = 3

print("Addition:\t", x, "+", y, "=", x+y)
print("Subtraction:\t", x, "-", y, "=", x-y)
print("Multiplication:\t", x, "*", y, "=", x*y)
print("Division:\t", x, "/", y, "=", x/y)
print("Floor division:\t", x, "//", y, "=", x//y)
print("Reminder:\t", x, "%", y, "=", x%y)
print("Exponent:\t", x, "**", y, "=", x**y)

print("")

b=3
a=b
print("Assign value:\t\t", "a=", a)
a+=b
print("Add & assign:\t\t", "a=", a, " \t\t(3+3)" )
a-=b
print("Subtract & assign:\t", "a=", a, "\t\t(6-3)" )
a*=b
print("Multiply & assign:\t", "a=", a, "\t\t(3*3)" )
a/=b
print("Divide & assign:\t", "a=", a, "\t(9/3)" )
a%=b
print("Remainder & assign:\t", "a=", a, "\t(3%3)" )
b**=3
print("Exponent & assign:\t", "b=", b, "\t\t(3**3)")

#string manipulation
print("")

s1 = "Hello"
s2 = "World"
print("s1+s2 is:\t", s1+s2)
print("s1*2 is:\t", s1*2)
print("s1[1] is:\t", s1[1])
print("s1[1:3] is:\t", s1[1:3])
print("Is H in s1?\t", ("H" in s1))
print("Is h in s1?\t", "h" in s1)
print("is h not in s1?\t", "h" not in s1 )

# string method example 
print("")

s1 ="Learning Python program in easy steps"
s2=s1.replace("program", "coding")
print(s2)
gnum = s1.count("g")
print("The number of occurance of g is", gnum)
p_index = s1.find("P")
print("The index of the first occurance of P is", p_index)

# Additional string method example 
print("")

a="12"
b="12.3"
c="number"
d="    "
print("Is a digit?\t", a.isdigit() )
print("Is b decimal?\t", a.isdecimal() )
print("Is b digit?\t", b.isdigit() )
print("Is b decimal?\t", b.isdecimal() )
print("Is c digit?\t", c.isdigit() )
print("Is d space?\t", d.isspace() )

#Additional string method example 2
print("")

s1="      Hello World     "
s2="|"
s3=s1.lstrip()
print(s2+s3+s2)
s3=s1.rstrip()
print(s2+s3+s2)
s3=s1.strip()
print(s2+s3+s2)

#Additional string method example 3
print("")

s1="Hello Word"
s2=s1.center(20, "*")
print(s2)
s2=s1.ljust(20, "*")
print(s2)
s2=s1.rjust(20, "*")
print(s2)
