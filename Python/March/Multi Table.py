"""
Multiplication Table of user through number.
Date : 19.03.2024
"""
import os

os.system('clear')
n = int(input("Enter a number: "))
print (f"\nMultiplication Table of {n}\n")
for i in range(1, 11):
    print (n, "x", i, "=", n*i)
     