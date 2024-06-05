"""
Choose weather to break or continue (multiple times). Then choose multiple letters to ignore.
Date: 16.03.2024
"""
import os

os.system('clear')
word = input("Enter a word: ")
print ("Choose 1 for 'break'")
print ("Choose 2 for 'continue'")
d = int(input("Choose: "))
print("")
c = []  
if d == 2:
    ignore = int(input("How many letters to ignore: "))
    for i in range(ignore):
        letter = input(f"Enter letter {i+1}/{ignore}: ")
        c += {letter}           # Add letter to the list
        if letter not in word:
            print("Letter not found")
            continue 
    r_word = ""
    for letter in word:
        if letter in c:
            continue
        r_word += letter
    print(r_word)
elif d == 1:
    letter = input("Enter letter to break: ")
    if letter not in word:
        print("Letter not found")
        exit()
    n = int(input("Enter occurrence to break: "))
    count = 0
    for i in range (0,len(word)):
        if word[i] == letter:
            count += 1
            if count == n:
                break
        else:
            print(word[i], end= '')
else:
    print("Invalid choice!")

        


