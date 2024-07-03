"""
Dictionary - 
    - A dictionary is a collection which is unordered, mutable, and indexed.
    - In Python dictionaries are written with curly brackets, and they have keys and values.
    - Function:
        - clear()    - Removes all the elements from the dictionary
        - copy()    - Returns a copy of the dictionary
        - fromkeys()    - Returns a dictionary with the specified keys and value
        - get()    - Returns the value of the specified key
        - items()    - Returns a list containing a tuple for each key value pair
        - keys()    - Returns a list containing the dictionary's keys
        - pop()    - Removes the element with the specified key
        - popitem()    - Removes the last inserted key-value pair
        - setdefault()    - Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
        - update()    - Updates the dictionary with the specified key-value pairs
        - values()    - Returns a list of all the values in the dictionary
Date : 7.3.2024
Date : 27.3.2024           [UPDATED] 
"""
import os

os.system('clear')

a = {"Het": 18, "Kshitij": 19, "Eshan": 20, "Abhay": 19}    # Original dictionary
"""
print(a)
input()
print(a.keys())
input()
print(a.values())
input()

print(a["Het"])    # Slice the value of the key "Het"
input()

a["Eshan"] = 40      # Add a new key "Eshan" with value 40
print(a)
input()
a["Eshan"] = 50      # Change the value of the key "Eshan" to 50
print(a)
input()
print(type(a))
input()
print(a["Het"]*2)  # Multiply the value of the key "Age1" by 2
input()
a.pop("Het")       # Remove the key "Het" from the dictionary
print(a)
input()
a.popitem()         # Remove the last key-value pair from the dictionary
print(a)
input()
"""
# Updated on 27.3.2024.
v = list(a.values())        # Convert the values of the dictionary into a list
w = list(a.keys())          # Convert the keys of the dictionary into a list
print("List of values: ",v)
print("List of keys: ",w)
print()

# Sort the values then print values and keys of values in for loop.
v.sort()
keys = []                   # List to store keys that have already been printed
for i in v:
    print(i,end=": ")
    for j in w:
        if a[j] == i and j not in keys:
            print(j+" ",end="| ")
            keys.append(j)  # Add the key to the list of printed keys
            break
"""
age = a.copy()    # Copy the dictionary
age = {"Het" : 19}    # New dictionary
print("New Dictionary: ",age)
a.update(age)    # Update the dictionary with the original dictionary
print("Updated Dictionary: ",a)   # Add the original dictionary at the end of new dictionary
print(a.get("Het"))    # Get the value of the key "Het"
print(a.items())    # Get the key-value pair
item = a.items
for i in a.items():    # Print the key-value pair
    print(i)
for i in a:    # Print the keys
    print(i+" ",end="")
"""
