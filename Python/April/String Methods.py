"""
String  [Detailed]  -
        Use of inbuilt string methods

Date : 03.04.2024
"""
import os

os.system('clear')
a = "Hello World World"
# 1. \\ Count() - Counts the number of times a sub-string appears in the string.
print("Count: ",a.count("World",0,5))
# 2. \\ Find() - Returns the index of the first occurrence of the sub-string.
print("Find: ",a.find("World"))
# 3. \\ Rfind() - Returns the index of the last occurrence of the sub-string.
print("Rfind: ",a.rfind("World"))
# 4. \\ Capitalize() - Capitalizes the first letter of the string.
print("Capitalize: ",a.capitalize())
# 5. \\ Title() - Capitalizes the first letter of each word in the string.
print("Title: ",a.title())
# 6. \\ Upper() - Converts the string into uppercase.
print("Upper: ",a.upper())
# 7. \\ Lower() - Converts the string into lowercase.
print("Lower: ",a.lower())
# 8. \\ Swapcase() - Swaps the case of the string.
print("Swapcase: ",a.swapcase())
# 9. \\ Isalnum() - Returns True if all characters in the string are alphanumeric.
print("Isalnum: ",a.isalnum())
# 10. \\ Isalpha() - Returns True if all characters in the string are alphabetic.
print("Isalpha: ",a.isalpha())
# 11. \\ Isdigit() - Returns True if all characters in the string are digits.
print("Isdigit: ",a.isdigit())
# 12. \\ Isnumeric() - Returns True if all characters in the string are numeric.
print("Isnumeric: ",a.isnumeric())
# 13  \\ Center() - Returns a centered string.
print("Center: ",a.center(50))
# 14. \\ isupper() - Returns True if all characters in the string are uppercase.
print("isuuper: ",a.isupper())
# 15. \\ islower() - Returns True if all characters in the string are lowercase.
print("islower: ",a.islower())
# 16. \\ istitle() - Returns True if the string follows the rules of a title.
print("istitle: ",a.istitle())
# 17. \\ replace() - Replaces a sub-string with another sub-string.
print("Replace: ",a.replace("World","Python " * 3,1))
# 16. \\ Strip() - Removes any leading (spaces at the beginning) and trailing (spaces at the end) characters (space is the default leading character to remove).
print("Strip: ",a.strip())
# 17. \\ Lstrip() - Removes any leading (spaces at the beginning) characters (space is the default leading character to remove).
print("Lstrip: ",a.lstrip())
# 18. \\ Rstrip() - Removes any trailing (spaces at the end) characters (space is the default leading character to remove).
print("Rstrip: ",a.rstrip())
# 19. \\ Partition() - Returns a tuple where the string is parted into three parts.
print("Partition: ",a.partition("World"))
# 20. \\ Joint() - Joins the elements of an iterable to the end of the string.
print("Joint: ","-".join(a))
# 21. \\ isspace() - Returns True if all characters in the string are whitespaces.
print("Isspace: ",a.isspace())
# 22. \\ startswith() - Returns True if the string starts with the specified value.
print("Startswith: ",a.startswith("Hello"))
# 23. \\ endswith() - Returns True if the string ends with the specified value.
print("Endswith: ",a.endswith("World"))
"""
24. \\ Encode() - Returns an encoded version of the string.
                 - The encoding parameter can be used to specify the encoding.
                    - ASCII , UTF-8 (default).
                 - The errors parameter can be used to handle the errors.
                    - backslashreplace - uses a backslash instead of the character that could not be encoded.
                    - ignore - ignores the characters that cannot be encoded.
                    - replace - replaces the character with a questionmark.
                    - namereplace - replaces the character with a text explaining the character. 
                    - xmlcharrefreplace - replaces the character with an XML character.
"""
print("Encode: ",a.encode(encoding = "ASCII",errors = "ignore"))
"""
25. \\ Decode() - Returns a decoded version of the string.
                        - Decodes the string using the codec registered for encoding.
"""
print("Decode: ",a.encode(encoding = "ASCII",errors = "ignore").decode(encoding = "ASCII",errors = "ignore"))
