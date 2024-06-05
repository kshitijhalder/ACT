"""
List: 
    - List is a collection of items
    - List is ordered
    - List is changeable
    - List allows duplicate values
    - List is written in square brackets
    - List is used to perform mathematical operations
    - List is used to remove duplicate values from a list
Date : 5.3.2024
"""
import os

os.system('clear')
#Original list
list1 = [1,2,3,4,5,6,7,8,9,10]
print(list1)
input()
print(list1[0])    #Prints the first element of the list
input()
print(list1[9])    #Prints the last element of the list
input()
#Basic Slicing
print(list1[0:5])    #Prints the first 5 elements of the list
input()
print(list1[5:])    #Prints the elements from 6th to last of the list
input()
#Negative Slicing
print(list1[-1])    #Prints the last element of the list
input()
print(list1[:-5])    #Prints the first 5 elements of the list
input()
print(list1[-5:])    #Prints the last 5 elements of the list
input()
#Changing the elements of the list
list1[0] = 11    #Changes the first element of the list to 11
print(list1)
input()
#Slicing with step
print(list1[0:10:2])    #Prints the elements of the list with step 2
