"""
Relational Operator
- It is used to compare two values.
- It returns a boolean value.       (True or False)
Date: 11.3.2024
"""
import os

os.system('clear')
# Boolean value IF value is from 15 to 35 
num = int(input("Enter a number: "))
result = num >= 15 and num <= 35
print(result)