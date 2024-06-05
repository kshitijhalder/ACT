"""
Bitwise Operator
                
                - It is used to compare binary numbers.
                - It returns a binary value.    (eg. 0b1010 where 0b is the prefix for binary number)
                - And Operator: & (Returns 1 if both bits are 1)
                - Or Operator: | (Returns 1 if one of the bits is 1)
                - Xor Operator: ^ (Returns 0 when both bits are same)
                - Not Operator: ~ (Returns the complement of the number)
                - Left Shift Operator: << (Shifts the bits to the left)
                - Right Shift Operator: >> (Shifts the bits to the right)
Date: 12.3.2024
"""
import os

os.system('clear')                                       
a=int(input("Enter a number A: "))
b=int(input("Enter a number B: "))      
                                        
print("Binary of A is",bin(a))
print("Binary of B is",bin(b))
input()                 
"""
print(bin(a) & bin(b))      #Error
"""
print("And Operator: ",bin(a & b),a & b)
print("Or Operator: ",bin(a | b),a | b)
print("Xor Operator: ",bin(a ^ b),a ^ b)
print("Not Operator/ Compliment: ",bin(~a),~a)      
print("Left Shift Operator: ",bin(a << 2),a << 2)
print("Right Shift Operator: ",bin(a >> 2),a >> 2)
