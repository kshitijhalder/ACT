"""
Enter a number. Then left shift the number by 2 and print the sum of the original number 
and the left shifted number (using eval() function).
Date: 12.3.2024
"""
import os

os.system('clear')
a = int(input("Enter a number: "))
b = a << 2
print("\nLeft Shifted number is",b)
input()
print(eval("a+b"))