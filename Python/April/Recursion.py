""" 
Recursion - A function that calls itself
Date : 11.04.2024
     : 16.04.2024           [UPDATED]
"""

import os, re

os.system('clear')

def factorial(n):
    if n is 1:
        return 1
    elif n is 0:
        return 1
    else:
        return n * factorial(n-1) 

def sum(n):
    if n is 1:
        return 1
    elif n is 0:
        return 0
    else:
        return n + sum(n-1)
# Edited on: 16:04:2024    
def repeat(n,n2):
    if n2 is 1:
        return n
    elif n2 is 0:
        return 0
    else:
        return n + repeat(n,n2-1)
"""     
n = int(input("Enter a number: "))
print("Factorial of",n,"is",factorial(n))
print("Sum of",n,"natural numbers is",sum(n))
n2 = int(input("Enter a number: "))
print(f"Sum of {n} {n2} number of times is",repeat(n,n2))
"""
import os, re

os.system('clear')

Str_1 = "@We are learning Python 012@"
s = re.subn(r'\bPython\b', 'Java', Str_1)
print("Original String: ",Str_1)
print("Substituted String: ",s[0])
