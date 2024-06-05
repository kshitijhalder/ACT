"""
Use of list operators to create a list of squares in for loop.
Date: 22.03.2024
"""
import os

os.system('clear')
a = []
x = int(input("Enter the number: "))

for i in range(1, x + 1):
    a.append(i ** 2)

print(a)