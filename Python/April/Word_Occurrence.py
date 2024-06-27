"""
Count the number of occurrences of each word in a given sentence (string).
Date : 05.04.2024
"""
import os

os.system('clear')
Str_1 = input("Enter a sentence: ")

def word_occurrence(Str_1):
    """
    Str_2 = ""
    for i in Str_1.split():
        if i.isalpha() and i not in Str_2:
            Str_2 += i
            location = Str_1.find(i)
            c = Str_1.count(i)
            count = 0
            b = 0
            while count < c:
                b = Str_1.find(i,b)
                count += 1
                print(f"Word: {i} - Occurrence: {c} - Location: {b}")
                b += 1
    """
    sub_str = input("Enter a word: ")
    c = Str_1.count(sub_str)
    print("Word: ", sub_str, " - Occurrence: ", c, "Times at: ", end = "")
    str_2 = 0
    count = 0
    
    while count < c:
        str_2 = Str_1.find(sub_str, str_2)
        print(str_2, end =" ")
        str_2 += 1
        count += 1

word_occurrence(Str_1)