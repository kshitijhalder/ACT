import os

os.system('clear')
a  = {"one": 1, "two": 2, "three": 3}
print("Dictionary: ",a)
a ["four"] = 4
print("New Dictionary: ",a)
print(a.keys())
print(a.values())
a ["one"] = 5
print("Updated Dictionary: ",a)
del a
os.system('clear')

Age = { "Het": 19, "Abhay": 19, "Kshitij": 19, "Eshan": 20}
print("Dictionary: ",Age)
print(Age.keys())
print(Age.values())
Age.pop("Het")
print("Updated Dictionary: ",Age)
Age.popitem()
print(Age)
Age.clear()
print(Age)