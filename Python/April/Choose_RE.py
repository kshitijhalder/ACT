"""
Choose a function in module (RE) to perform the following operations:
    - match
    - search
    - split
    - findall
Then enter the regular expression to perform the above operations.
Date : 09.04.2024 
"""
import os, re

os.system('clear')
str_1 = "We are \nlearning Python"
print("Choose a module function from the following operations:")
print(" 1. match \n 2. search \n 3. split \n 4. findall")
choice = int(input("Enter your choice: "))
if choice == 1:
    choice_1 = input("Enter the regular expression: ")
    x = re.match(choice_1, str_1)
    print("Match: ",x)
elif choice == 2:
    choice_2 = input("Enter the regular expression: ")
    y = re.search(choice_2, str_1)
    print("Search: ",y)
elif choice == 3:
    choice_3 = input("Enter the regular expression: ")
    z = re.split(choice_3, str_1)
    print("Split: ",z)
elif choice == 4:
    choice_4 = input("Enter the regular expression: ")
    a = re.findall(choice_4, str_1)
    print("Findall: ",a)
else:
    print("Invalid choice")