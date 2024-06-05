"""
Delete if an element is repeated twice in a list. If it is repeated more than twice, do not delete.
Date: 23.03.2024
"""
import os

os.system('clear')
# Example list
numbers = [1, 2, 3, 4, 2, 5, 6, 3, 3, 7, 8, 8]

sorted_numbers = sorted(numbers)
print("Sorted List:", sorted_numbers)

twice = []

# Iterate through the list and remove elements repeated twice
for i in numbers:
    if numbers.count(i) == 2 and i not in twice:
        twice.append(i)

numbers_1 = list(i for i in numbers if i not in twice)

print ("\nList after removing elements repeated twice:", numbers_1)
print ("Twice: ", twice)