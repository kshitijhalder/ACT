"""
Assert - 
    - It is used to check the condition of the code.        
    - If the condition is true, the code will run.
    - If the condition is false, the code raise an error which is.
Question:   Enter two numbers A and B. Check if A & `B are odd numbers. If they are odd, then print the result of A/B.
Date : 19.03.2024
"""
import os

os.system('clear')
a = int(input("Enter a number A: "))    
assert a % 2 != 0, "Enter odd number"
# assert a % 2 == 0, "Enter even number"
b = int(input("Enter a number B: "))    
assert b % 2 != 0, "Enter odd number"
# assert b % 2 == 0, "Enter even number"
print (a/b)