"""
Identity Operator :
    1. is
    2. is not
Date : 13.3.2024
"""
import os

os.system('clear')
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a is b)  # False
print(a is not b)  # True

a=b
print(a is b)  # True
print(a is not b)  # False