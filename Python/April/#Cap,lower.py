"""
Number of Upper case and Lower case letters in a string
Date : 05.04.2024
"""
import os

os.system('clear')
str = input("Enter a string: ")
upper, lower, other = 0, 0, 0
for i in str:
    if i.isupper():
        upper += 1
    elif i.islower():
        lower += 1
    else:
        other += 1
print("Number of Upper case letters: ", upper, "\nNumber of Lower case letters: ", lower
      , "\nNumber of other characters: ", other)
