"""
Check if the string is in uppercase. If it is, convert it into lowercase.
Date : 05.04.2024
"""
import os

os.system('clear')
string = input("Enter a string: ")

if string.isupper():
    print("String is in uppercase")
    print("Converting string to lowercase: ", string.lower())

elif string.islower():
    print("String is in lowercase")
    
else:
    print("String is in mixed case")
    print("Converting string to lowercase: ", string.lower())