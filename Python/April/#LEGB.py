"""
LEGB - Local, Enclosing, Global, Built-in

Local: Names assigned in any way within a function (def or lambda), 
       and not declared global in that function.
Enclosing: Names in the local scope of any and all enclosing functions (def or lambda) 
"""
import os
import Keyword_Occ as a
import File_Methods as c

os.system("clear")

print(help(a))
x = input("Enter the file path: ")
b = a.count_keywords(x)
c.write_counts_to_file(b,"Python/April/Key_Occ.txt") 