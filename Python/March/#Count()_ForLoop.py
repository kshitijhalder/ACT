"""
Count the number of times a number appears in a list using for loop.
Date: 22.03.2024
"""
import os

os.system('clear')
a = [1,1,3,6,3,7,7,7]
print("List:", a)
print()
print ("Number   Count   Index")
print("------------------------")
c = []
for i in a:
    if i not in c:
        c.append(i)
        print(i, "     |", a.count(i), "     |", a.index(i) + 1)
