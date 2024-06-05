"""
Break, Pass & Continue - 
Date : 16.03.2024
"""
import os

os.system('clear')
a = input()
for i in range (0,len(a)):
    """
    print(a[i])         #Vertical
#    print(a[i], end= '')
    """
    if a[i] == 'l':             # ('is' equal to '==')
        #break
        continue
    else:
        print(a[i], end= '')
print("\nOut of the loop")
# Pass -
# for i in range (0,len(a)):
#     pass          #It will not give any error
        