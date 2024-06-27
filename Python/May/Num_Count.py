"""
Occurrence of each number in a list
"""
import os

os.system('clear')
a = [1,1,3,6,3,7,7,7]
print("List:", a)
print()
print ("Number | Count  | Index")
print("-------------------------")
c = []
for i in a:
    if i not in c:
        c.append(i)
        print(i, "     |", a.count(i), "     |", a.index(i) + 1)