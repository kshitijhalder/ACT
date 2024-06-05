"""
Special Sequences:
    - \A : Returns a match if the specified characters are at the beginning of the string
    - \b : Returns a match where the specified characters are at the beginning or at the end of a word
    - \B : Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word
    - \d : Returns a match where the string contains digits (numbers from 0-9)
    - \D : Returns a match where the string DOES NOT contain digits
    - \s : Returns a match where the string contains a white space character
    - \S : Returns a match where the string DOES NOT contain a white space character
    - \w : Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)
    - \W : Returns a match where the string DOES NOT contain any word characters
    - \Z : Returns a match if the specified characters are at the end of the string

Date : 10.04.2024
"""
import os, re

os.system('clear')
# 1.\\ '\s '
Str_1 = "@We are learning Python012@"
s = re.subn('\blearning\b', '_', Str_1)
print("Sub: ",Str_1)
print("Substitute: ",s)
""" 
max
min
round
int
 """