"""
2nd Largest and 2nd Smallest number in a using for loop. min() and max() functions.
Date: 23.03.2024
"""
import os

os.system('clear')
a = [9, 3, 6, 1, 5, 7, 2, 8, 4, 10]
print("List:", a)

largest = max(a)
smallest = min(a)

for i in a:
    if i == largest:
        a.remove(i)
        break
print("2nd Largest number is:", max(a))
for i in a:
    if i == smallest:
        a.remove(i)
        break
print("2nd Smallest number is:", min(a))

"""
ALTENATE METHOD:

a = [9, 3, 6, 1, 5, 7, 2, 8, 4, 10]
print("List:", a)

largest = max(a)
smallest = min(a)

a.remove(largest)               # Removes the largest number
a.remove(smallest)              # Removes the smallest number 

print("2nd Largest number is:", max(a))
print("2nd Smallest number is:", min(a))
"""