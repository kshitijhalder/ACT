"""
Aliasing - It is the phenomenon of giving multiple names to the same memory location.
Date : 22.03.2024
"""
import os

os.system('clear')
list = [1,2,3,4,5]
list_1 = list [ : 3]
print("The original list is: ",list)
print("The new list is: ",list_1)

# Copy() - Returns a copy of the list
print("\nCopy Function:\n")
a = [1,3,2,4,5]
b = a.copy()
print("B before: ",b)
b[0] = 10                   # Replacing the value of 0th index of b
print("B after: ",b)