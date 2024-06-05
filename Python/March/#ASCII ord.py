"""
ASCII - using ord() function
      - ord() function returns the ASCII value of the given character.
Date : 19.03.2024
"""
import os

os.system('clear')
a = input("Enter a string: ")
for i in a:
    print(f"ASCII value of {i} is {ord(i)}")
# or
for i in range(len(a)):
    print(f"ASCII value of {a[i]} is {ord(a[i])}")
