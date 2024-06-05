"""
Triangle using nested for loop
Number Triangle - 1-5
Date: 13.3.2024
"""
import os

os.system('clear')
n = 5
for i in range(1, n+1):
    row = ''
    for j in range(1, i+1):
        row += str(j) + ' '
    print(row)