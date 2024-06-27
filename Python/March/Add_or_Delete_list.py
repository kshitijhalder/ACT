"""
In a list, Choose to either add or delete an element.
Use the following functions:
* Append                    * Pop
* Extend                    * Remove
* Insert                    * Clear
Ask the user sub questions according to the function chosen.

Date : 20.03.2024
"""
import os

os.system('clear')
list = [1,2,3,4,5]
print("The original list is: ",list)
print("\nChoose to either add or remove an element on the list: ")
print("1 -> Add an element")
print("2 -> Remove an element")
choice_1 = int(input("Enter your choice: "))
if choice_1 == 1:
    print("\nChoose the function to add an element: ")
    print("1 -> Append")
    print("2 -> Extend")
    print("3 -> Insert")
    choice_2 = int(input("Enter your choice: "))
    if choice_2 == 1:
        element = input("Enter the sub-list to append: ")          # Taking string input from user
        #for i in element:
        #    list.append(i)  #type: ignore
        split_element = element.split()                            # Split the string into a list of strings
        list.append(split_element)   #type: ignore
        print("The list after appending is: ", list)
        """
        list_int = [int(i) for i in split_element]                 # Convert the list of strings to a list of integers
        list.append(list_int)   #type: ignore
        print("The list after appending is: ", list)
        """
    elif choice_2 == 2:
        element = int(input("Enter the element to extend: "))
        list.extend([element])  # Convert element to a list
        print("The list after extending is: ",list)
    elif choice_2 == 3:
        index = int(input("Enter the index to insert: "))
        element = int(input("Enter the element to insert: "))
        list.insert(index,element)
        print("The list after inserting is: ",list)
    else:
        print("Invalid choice")
elif choice_1 == 2:
    print("\nChoose the function to remove an element: ")
    print("1 -> Pop")
    print("2 -> Remove")
    print("3 -> Clear")
    choice_3 = int(input("Enter your choice: "))
    if choice_3 == 1:
        index = int(input("Enter the index to pop: "))
        popped = list.pop(index)
        print("The list after popping is: ",list)
        print("The popped element is: ",popped)
    elif choice_3 == 2:
        element = int(input("Enter the element to remove: "))
        list.remove(element)
        print("The list after removing is: ",list)
    elif choice_3 == 3:
        result = list.clear()
        print("The list after clearing is: ",result)        # None
        #print("The list after clearing is: ",list)         # []
    else:
        print("Invalid choice")
else:
    print("Invalid choice")