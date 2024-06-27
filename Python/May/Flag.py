import os
import numpy as np          #type: ignore

os.system('clear')


#Apple=mango
#print(Apple)

# Octal - 0o or 0O
# Hexadecimal - 0x or 0X
a = 0o123
print(a)

c = "INDIA"

for i in c:
    print("\t")
    print(i, end="\n\t")

def find_armstrong_numbers():
    armstrong_numbers = []
    for num in range(1, 100001):
        sum = 0
        temp = str(num)
        for digit in temp:
            sum += int(digit) ** len(temp)
        if num == sum:
            armstrong_numbers.append(num)
    return armstrong_numbers

print("All 3 digit Armstrong numbers are:")
for num in find_armstrong_numbers():
    print(num, end=", ")