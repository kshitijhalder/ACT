#Calculator -
#Create a simple calculator that first asks the user what method they would like to use (addition, subtraction, multiplication, division) and then asks the user for two numbers, returning the result of the method with the two numbers. Here is a sample prompt:
#Date : 7.3.2024
import os

os.system('clear')
print("\t\t\t\t\t\t\tCalculator\n\n")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exponentiation")
print("6. Floor Division")
a=int(input("\nEnter your choice : "))
print("\n") 
if a==1:
    b=float(input("Enter the first number : "))
    c=float(input("Enter the second number : "))
    print("\nThe sum is",b+c)
elif a==2:
    b=float(input("Enter the first number : "))
    c=float(input("Enter the second number : "))
    print("\nThe difference is",b-c)
elif a==3:
    b=float(input("Enter the first number : "))
    c=float(input("Enter the second number : "))
    print("\nThe product is",b*c)
elif a==4:
    b=float(input("Enter the first number : "))
    c=float(input("Enter the second number : "))
    print("\nThe quotient is",b/c)
elif a==5:
    b=float(input("Enter the base : "))
    c=float(input("Enter the exponent : "))
    print("\nThe result is",b**c)
elif a==6:
    b=float(input("Enter the first number : "))
    c=float(input("Enter the second number : "))
    print("\nThe result is",b//c)
else:
    print("Invalid choice")
