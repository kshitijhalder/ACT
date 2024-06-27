"""
Check if the string is title or not. If it is, convert it into capital case.
Date : 05.04.2024
"""
import os

os.system('clear')
string = input("Enter a string: ")

if string.istitle():
    print("String is in title case")
    print("Converting string to capital case: ", string.capitalize())
elif string.islower() or string.isupper():
    if string.islower():
        print("String is in lowercase")
    if string.isupper():
        print("String is in uppercase")
else:
    print("String is in mixed case")
