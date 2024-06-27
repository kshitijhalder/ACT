"""
Tuple in descending order
Date : 23.3.2024
"""
import os

os.system('clear')
a = (9, 3, 6, 1, 5, 7, 2, 8, 4, 10)
print("Tuple: ", a)
a = sorted(a, reverse=True)
a = tuple(a)
print("Tuple in descending order: ", a)
