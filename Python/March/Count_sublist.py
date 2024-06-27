"""
Count the number of times a number appears in sub-list inside list using for loop.
Date: 22.03.2024    
"""
import os

os.system('clear')
a = [1, 2, 3, [7, 7, 7, 5, 5, 2, 2, 1]]
print("List:", a)
print()
print("Number   Count")
print("---------------")
c = []
for sub_list in a:
    if type(sub_list) == list:  # Check if element is a list
        for element in sub_list:
            if element not in c:
                c.append(element)
                print(element, "     |", sub_list.count(element))
