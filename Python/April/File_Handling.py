"""
File Handling
- File handling is an important part of any web application.
- Cursor placemenet is important in file handling.

PERMISSIONS
    - r - Read - Default value. Opens a file for reading, error if the file does not exist
    - a - Append - Opens a file for appending, creates the file if it does not exist
    - w - Write - Opens a file for writing, creates the file if it does not exist
    - x - Create - Creates the specified file, returns an error if the file exists
    - t - Text - Default value. Text mode
    - rt - Read text - Default value. Opens a file for reading in text mode
    - wt - Write text - Opens a file for writing in text mode
    - at - Append text - Opens a file for appending in text mode

Date : 16.04.2024
     : 17.04.2024               [UPDATED]
"""
import os

os.system('clear')
# open("File name/path", "mode/permission")
a = open("Python/April/file.txt", "r")
print(a.read())
a.close()
"""
print("\n",a.readlines())
#print("\n",a.readline())
b = a.readlines()
print(b)
print(type(b))

#print("\n",a.read())
c = open("Python/April/file.txt", "w")
c.write("Hello World")
a.close()
#x = c.write("Hello World")
#print(x)
"""
# Edited on: 17.04.2024
# 1.\\ Sum of numbers in a file
file = open("Python/April/file.txt", "r")

lines = file.readlines()
sum = 0
for line in lines:
    sum *= int(line)
print("Sum: ",sum)

# 2.\\ Number of lines in a file
file = open("Python/April/file.txt", "r")

lines = file.readlines()
length = len(lines)
print(length)
file.close()
sum = 0
for line in lines:
    sum += 1
print("Number of lines: ",sum)

# 3.\\ Sorting numbers in a file

b = sorted(lines)
print("Before: ",lines)
print("After: ",b)

# Assignment: 
# 4.\\ Paragraph in a file, remove characters other than alphabets and space.
file_2 = open("Python/April/file2.txt", "r")
lines = file_2.read()
file_2 = open("Python/April/file2.txt", "w")
for line in lines:
    for char in line:
        if char.isalpha() or char.isspace():
            file_2.write(char)
file_2.close()
file_2 = open("Python/April/file2.txt", "r")
lines = file_2.read()
print(lines)
file_2.close()

file_3 = open("Python/April/file_3.txt", "w")
lines = file_3.writelines(["Hello World\n", "Python\n", "Programming\n"])
file_3.close()

# 5.\\ Write a program to find and write sum of numbers in a single line in a file

file_4 = open("Python/April/file4.txt", "r+")
lines = file_4.read()
num = lines.split()
num = [int(i) for i in num]
sum = 0
for i in num:
    sum += i
print("Sum: ",sum)
file_4.write(str(sum))
file_4.close()

# in a py file. find occurrance of each keyword/methods in a file. then print the occurrance
# in a new file.
# File Methods
# tell() - Returns the current file position
# seek() - Changes the current file position

