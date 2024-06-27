"""
Pyramid using nested for loop
Date: 13.3.2024
"""
import os

os.system('clear')
n = 5
for i in range(1, n+1):             
    row = ' '
    for j in range(n-i):
        row += ' '
    for j in range(i):
        row += '* '
    print(row)
    