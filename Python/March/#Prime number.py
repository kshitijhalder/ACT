#Use of Boolean values
#Date: 5.3.2024
import os

os.system('clear')
a=int(input("Enter a number: "))        #Taking input from user
y=False                                 #Initialising a boolean variable
if a>1:                                 #Checking if the number is greater than 1
    for i in range(2,a):                #Checking for the factors of the number
        if a%i==0:                      #Checking if the number is divisible by any other number
            y=True                      #Changing the value of the boolean variable
            break
    if y==True:                         #Checking the value of the boolean variable
        print("The number is not prime")      
    else:
        print("The number is prime")   
else:
    print("The number is not prime")   