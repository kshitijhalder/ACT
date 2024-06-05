"""
LIST - Detailed                                                                                 #UPDATED
    1. List is a collection which is ordered and changeable. Allows duplicate members.
    2. Three types of Function in List:
        - append() - Adds an element at the end of the list
        - clear() - Removes all the elements from the list
        - copy() - Returns a copy of the list
        - count() - Returns the number of elements with the specified value
        - extend() - Add the elements of a list (or any iterable), to the end of the current list
        - index() - Returns the index of the first element with the specified value
        - insert() - Adds an element at the specified position
        - max() - Returns the largest item in an iterable
        - min() - Returns the smallest item in an iterable
        - pop() - Removes the element at the specified position
        - remove() - Removes the first item with the specified value
        - reverse() - Reverses the order of the list
        - reversed() - string as input and returns a list (by using list()) as output
        - sort() - Sorts the list
        - sorted() - Returns a new sorted list
        - split() - Splits the string into a list

Date : 19.03.2024
Date : 20.03.2024   [Updated]
Date : 22.03.2024   [Updated]
"""
import os

os.system('clear')

# 1.\\ Split() - Splits the string into a list
print ("Split Function:\n")
a = "Hello, python"
x= a.split(",") # ['Hello', ' python']
print (x,"Type: ", type(x))
x, y = a.split(",") # x = 'Hello', y = ' python'
print (x,y,type(x),type(y))

# 2.\\ Append() - Adds an element at the end of the list
a = [1,2,3,4,5]
b = ["Hello","a"]
print ("\nAppend Function:\n")
print ("A is: ",a,"\nB is: ",b)
a.append(b)     # type: ignore
print ("A is: ",a)


# 3.\\ Extend() - Add the elements of a list (or any iterable), to the end of the current list
#               - Extend can't add a single element, it can only add an iterable unlike append()
a = [1,2,3,4,5]
b = [6,7,8,9,10]
print ("\nExtend Function:\n")
a.extend(b)
print ("A is: ",a)

# 4.\\ Insert() - Adds an element at the specified position
a = [1,2,3,4,5]
print ("\nInsert Function:\n")
print ("A before: ",a)
a.insert(2,0)
print ("A after: ",a)

# Updated on 20.03.2024
# 5.\\ Pop() - Removes and returns the element at the specified index. 
#             If no index is specified, it removes and returns the last element in the list.
a = [1,2,3,4,5]
print("\nPop Function:\n")
print("A before: ",a)
b = a.pop()             # Removes the last element
print("Pop: ",b)
print("A after: ",a)

# 6.\\ Remove() - Removes the first item with the specified value
print("\nRemove Function:\n")
a = [1,3,2,3,4,5]
print("A before: ",a)
a.remove(3)
print("A after: ",a)

# 7.\\ Clear() - Removes all the elements from the list
print("\nClear Function:\n")
a = [1,2,3,4,5]
b = a.clear()
print("After clear(): ",b)      # None
print("After clear(): ",a)      # []

# 8.\\ Sort() - Sorts the list
print("\nSort Function:\n")
a = [1,3,4,2,5]
print("Before: ",a)
a.sort()
print("Ascending: ",a)
a.sort(reverse = True)      # use of argument - reverse
print("Descending: ",a)
b = ["a","c","f","d","b","e"]
b.sort()
print("Ascending: ",b)
c = ["Hello","Python","World","I","am","here"]
c.sort(key = len)           # use of argument - key
print("Ascending: ",c)

# 9.\\ Sorted() - Returns a new sorted list
print("\nSorted Function:\n")
a = [1,3,4,2,5]
print("Before: ",a)
b = sorted(a)  
print("After: ",b)          # Ascending
print(a)                    # Original list

# 10.\\ Reverse() - Reverses the order of the list
a = [1,3,2,4,5]
print("\nReverse Function:\n")
print("Before: ",a)
a.reverse()
print("After: ",a)

# 11.\\ Reversed() - Returns a reversed iterator
#                  - It uses string as input (argument) and returns a list as output (using list() function)
a = [1,3,2,4,5]
print("\nReversed Function:\n")
print("Before: ",a)
b = reversed(a)
#b = list(reversed(a))
print("After: ",list(b))     # Ascending    # use of list() function
print(a)                    # Original list

# 12.\\ Max() - Returns the largest item in an iterable
a = [1,3,2,4,5]
print("\nMax Function:\n")
print("A is: ",a)
print("Max no.: ",max(a))
b = ["a","c","f","d","b","e"]
print("\nB is: ",b)
print("Max alphabet: ", max(b))   
c = [2,4,3]
print("\nBiggest list: ",max(a,c))    

# 13.\\ Min() - Returns the smallest item in an iterable
print("\nMin Function:\n")
print("A is: ",a)
print("Min no.: ",min(a))
print("\nB is: ",b)
print("Min alphabet: ", min(b))

# Max() and Min() functions compares the individual elements of the lists in iteration (0 to __).
# If the list contains another list, then it will compare the first element of each list in

# 14.\\ Count() - Returns the number of elements with the specified value
a = [1,3,2,4,5,3,3]
print("\nCount Function:\n")
print("A is: ",a)
print("Count of 3: ",a.count(3))
print("Count of 6: ",a.count(6))

#Updated on 22.03.2024
# 15.\\ Copy() - Returns a copy of the list
print("\nCopy Function:\n")
a = [1,3,2,4,5]
b = a.copy()
print("B before: ",b)
b[0] = 10                   # Replacing the value of 0th index of b
print("B after: ",b)
