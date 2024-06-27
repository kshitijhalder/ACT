"""
Check if the value of a is changed in the following code:
"""
import os

os.system('clear')

def add(a,b):
    a = 5           # This is a local variable
    print(a+b)

a = 6               # This is a global variable
b = 7
add(a,b)
print(a)

a = int(input("Enter a string: "))
b = int(input("Enter another string: ")) 
print(a+b)