"""
Functions in Functions :
    - A function can be called inside another function.
    - The inner function can access, modify and return the outer function's variables.
    
"""
import os

os.system('clear')

def multiply(a, b, c):
    def add(a, b):
        return a + b
    print(f"\nSum of {a} and {b} is: ",add(a, b))
    return add(a, b) * c
    
a = int(input("Enter first number: ")) 
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))   

print("Product: ",multiply(a, b, c))