"""
Enter 4 elements. Using user-defined function, compile the elements into either list,
string or tuple (user choice).

Date: 30.03.2024
"""
import os

os.system('clear')

def list_(a,b,c,d):
    x = [a,b,c,d]
    print("List: ", x,"\nType: ",type(x))

def string_(a,b,c,d):
    x = f"{a}{b}{c}{d}"
    print("String: ",x,"\nType: ",type(x))

def tuple_(a,b,c,d):
    x = (a,b,c,d)
    print("Tuple: ",x,"\nType: ",type(x))
              
print("Enter 4 elements: ")
a = input("\nEnter 1st element: ")
b = input("Enter 2nd element: ")
c = input("Enter 3rd element: ")
d = input("Enter 4th element: ")
type_ = input("Enter the data type to compile the elements: ")

if type_ == 'list':
    list_(a, b, c, d)
elif type_ == 'string':
    string_(a, b, c, d)
elif type_ == 'tuple':
    tuple_(a, b, c, d)
else:
    print("Invalid choice")
