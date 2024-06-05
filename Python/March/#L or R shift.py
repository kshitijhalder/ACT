"""
Enter a number. Then choose whether to left shift or right shift the number and then print the shifted number.
Date : 13.3.2024
"""
import os

os.system('clear')
a = int(input("Enter a number: "))
b = int(input("Enter 1 for left shift and 2 for right shift: "))
if b == 1:
    c = int(input("Enter the number of bits to shift left: "))
    print("\nLeft Shifted number is",a << c)
else:
    c = int(input("Enter the number of bits to shift right: "))
    print("\nRight Shifted number is",a >> c)
 