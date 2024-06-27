"""
BEDMAS - Brackets, Exponents, Division and Multiplication, Addition and Subtraction
       - This is a simple program to demonstrate the order of operations in Python.
Date: 13.3.2024
"""
import os

os.system('clear')
a = ((3 // 5) * 6) / 5 * (5 ** 2)
print("Answer of is ",a)  
input()
print("Prove that python follows BEDMAS:")
step_1 = (3 // 5) * 6
print("Step 1 result:", step_1)  

step_2 = 5 ** 2
print("Step 2 result:", step_2)  

step_3 = step_1 / 5
print("Step 3 result:", step_3)  

step_4 = step_3 * step_2
print("Final result:", step_4)  
input()
print("\nNow compare the final result with the original result\n")

if a == step_4:
    print("Python follows BEDMAS")
else:
    print("Python does not follow BEDMAS")