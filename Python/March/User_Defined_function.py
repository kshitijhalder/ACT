"""
User Defined Function       
    - def (define) keyword is used to define a function.
Date : 30.03.2024
"""
import os

os.system('clear')

def printf():
    print("Hello World")

def add(a):
    print(eval(a))
  
def square(a):
    print(a**2)

def table(n):
    print(f"\nMultiplication Table of {n}\n")
    for i in range(1, 11):
        print (n, "x", i, "=", n*i)

def search(a):
    print("Searching for",a)
    flag = False
    for i in list1:
        """
        if i == a:
            print("Found")
            break
    else:
        print("Not Found")
    
        if i != a:
            continue
        else:
            print("Found")
        break
    else:
        print("Not Found")
"""
    if i == a:
        print("Found")
        flag = True

    if flag == False:
        print("Not Found")
    else:
        print("Found")
"""
a = input("Enter a number: ")
#add(a)
#printf()
#square(2)
"""

list1 = [11,12,13,14,15,16,17,18,19,20]
a = int(input("Enter a number: "))
#table(a)
search(a)