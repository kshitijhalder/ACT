"""
For Loop - 3
Sum of 'n' numbers. Find if sum is odd or even.
Date : 5.3.2024
"""
import os

os.system('clear')
sum = 0
n = int(input("Enter the number of elements : "))
for i in range (1,n+1):
    print(i)
    sum = sum + i
input()
print("Sum of",n,"numbers is",sum)
input()
if sum % 2 == 0:
    print("Sum is even")
else:
    print("Sum is odd")