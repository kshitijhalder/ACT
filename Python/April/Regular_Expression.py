"""
Regular Expression:
    - Regular expression is a sequence of characters that forms a search pattern.
    - It is used to check if a string contains the specified search pattern.
    - Regular expression can be used to perform all types of text search and 
      text replace operations.
      match and search
Date : 05.04.2024
"""
import os
import re               # Regular Expression module

os.system('clear')
Str_1 = "ee\ncdcdff"
Str_2 = "ice"
"""
Metacharacters:
    - Metacharacters are characters with a special meaning.
    - Metacharacters are used to define the search pattern.
    - [] : A set of characters
    - \ : Signals a special sequence (can also be used to escape special characters)
    - . : Any character (except newline character)
    - ^ : Matches the start of the string
    - $ : Matches the end of the string
    - * : Zero or more occurrences
    - ? : Zero or one occurrence
    - + : One or more occurrences
    - {} : Exactly the specified number of occurrences
    - | : Either or
    - () : Capture and group

flag = 0 
for i in Str_1:
    x = re.match('[a-d]', i) 
    if not x:
        flag = 1
if flag == 1:
    print("Pattern not match")
else:
    print("Pattern match")
"""
print("Str_1: ",Str_1)
x = re.findall('[a-d]', Str_1) 
print("Findall: ",x)
y = re.search('[a-d]', Str_1) 
print("Search: ",y)
z = re.split('[a-d]', Str_1, 1)
print("Split:",z)
a = re.match('[a-d]', Str_1)
print("Match: ",a)
        

        
        
"""   
if re.findall('[a-d]', Str_1):    # (Str_2, Str_1),('^ic'),('el{2}'),('^a.*l$')
    print("Both strings are same")
else:
    print("Both strings are different")
"""