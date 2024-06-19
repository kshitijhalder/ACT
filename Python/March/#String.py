"""
String - " "
       - A string is a sequence of characters enclosed within single or double quotes.
         - Strings are immutable.
            - Strings are ordered.
                - Strings are indexed.
                    - Strings are iterable.
             
Date : 5.3.2024
Date : 28.3.2024           [UPDATED]
"""
import os

os.system('clear')
a = input("Enter a string: ")
b = input("Enter another string: ")


# 1.\\ Prints the string 3 times
print(a*3)  

# Updated on 28.3.2024
# 2.\\ Concatenates the two strings
print(a+b)  

# 3.\\ Prints the length of the string
print(len(a))

# 4.\\ Prints the first character of the string
print(a[0])

# 5.\\ Prints the last character of the string
print(a[-1])

# 6.\\ Prints the characters from 3rd to 5th
print(a[2:5])

# 7.\\ Prints the string in reverse
print("Reverse",a[::-1])

# 8.\\ Prints the string in reverse and then concatenates it with the original string
print(a[::-1]+a)

# 9.\\ Prints Slice of the string
print(a[2:])

# 10.\\ Check if the strings are anagrams                             (Anagram - A word or phrase that is formed by rearranging the letters of another word or phrase, using all the original letters exactly once)
print()
a = list(a)
print(a)
b = list(b)
sorted_a = sorted(a)
sorted_b = sorted(b)
sorted_a = "".join(sorted_a)
sorted_b = "".join(sorted_b)
print("Sorted a: ",sorted_a) 
print("Sorted b: ",sorted_b)
if sorted_a == sorted_b:
    print("The strings are anagrams")
else:
    print("The strings are not anagrams")

# 11.\\ Check if the strings are palindromes
if a == a[::-1]:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")