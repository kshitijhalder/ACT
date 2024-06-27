"""
Create strings of 5 then merge them into a list.
Date: 19.3.2024
"""
import os

os.system('clear')
Str_1 = "range, type, len, ord, for"
Str_2 = "in, is, print, input, int"
Str_3 = "str, chr, bin, eval, break"
Str_4 = "continue, pass, assert,append,extend"
Str_5 = "insert, pop, remove, clear, sort"
Str_6 = "reverse, count, split, min, max"

List_1 = Str_1.split(",")
List_2 = Str_2.split(",")
List_3 = Str_3.split(",")
List_4 = Str_4.split(",")
List_5 = Str_5.split(",")
List_6 = Str_6.split(",")

#List_1.extend(List_2 + List_3 + List_4 + List_5 + List_6)
List_1.extend(List_2)
List_1.extend(List_3)
List_1.extend(List_4)
List_1.extend(List_5)
List_1.extend(List_6)
print(List_1) 