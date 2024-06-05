"""
Eval function
The eval() function evaluates the specified expression, if the expression is a legal Python statement, it will be executed.
Date: 12.3.2024
"""
import os

os.system('clear')
a = input("Enter an expression: ")
print("The result of the expression is:", eval(a))
#print(f"The result of {a} is:", eval(a)) 
