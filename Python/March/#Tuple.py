"""
Tuple - ordered, immutable, allows duplicate elements
        - Tuple is written in round brackets
        Topics covered -
                        1. Type of Tuple
                        2. Heterogeneous Data Types

Date : 23.3.2024
"""
import os

os.system('clear')

a = 1,3,5,2,4      #or (1,3,5,2,4)       #Tuple with same data types (homogeneous)

print ("A: ",type(a))

b = (1, 2, 3.4, "Hello", 3+4j)           #Tuple with different data types (heteregenous)
print ("B: ",b)

#a [ 0 ] = 10        #TypeError: 'tuple' object does not support item assignment
#print (a)

# 1.\\ Slicing
print ("A after Slicing: ",a [ : 3 : 2])

# 2.\\ Concatenation
c = a + b
print ("C: ",c)

"""
# 3.\\ Deletion
del a
print (a)       #NameError: name 'a' is not defined
"""

# 4.\\ Repetition
d = b * 2
print ("D: ",d)

# 5.\\ Typecasting 
e = list(b)
print ("E: ",e)

# 6.\\ Sorting
f = sorted(a)                   #sorted() returns a new sorted list
f = tuple(f)
print ("Sorted A: ",f)
a = list(a)                     #sort() sorts the list itself
a.sort()
print ("Sort A: ",tuple(a))

# 7.\\ Length
print ("Length of A: ",len(a))

# 8.\\ Maximum and Minimum
print ("Maximum of A: ",max(a))
print ("Minimum of A: ",min(a))