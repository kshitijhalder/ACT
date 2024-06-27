""" 
Use of math module in Python.
Numeric Functions : 

        * abs() : Returns the absolute value of a number.
        * max() : Returns the largest of the given arguments or items in an iterable.
        * min() : Returns the smallest of the given arguments or items in an iterable.
        * round() : Rounds a floating-point value.
        * pow() : Returns the value of x to the power of y.
        * int() : Returns an integer number.
        * ceil() : Returns the smallest integer greater than or equal to a number.
        * floor() : Returns the largest integer less than or equal to a number.
        * sqrt() : Returns the square root of a number.
        * fabs() : Returns the absolute value of a floating-point number.
        * factorial() : Returns the factorial of a number.
        * fmod() / remainder() : Returns the remainder of x/y.      [floating point modulus]
        * gcd() : Returns the greatest common divisor of two integers.
        * divmod() : Returns the quotient and the remainder when argument1 is divided by argument2.
        * exp() : Returns E raised to the power of x.
import datetime
                - date : Returns the current local date.
                - time : Returns the current local time.
                - datetime : Returns the current local date and time.

Date : 10.04.2024
"""
import os, math, random, datetime
from datetime import date, time, datetime

os.system('clear')
"""
# ceil()
a = 5.23
b = math.ceil(a)
print(b)
# round()
a = 5.23
b = round(a)
print(b)
# int()
a = 5.623
b = int(a)
print(b)
# max()
a = [10 , 40 , 30]
b = [20 , 30]
c = [30 , 20]
d = max(a)
print(d)
# abs()
a = -7.25
b = abs(a)
print(b)
# fabs()
a = -7.25
b = math.fabs(a)
print(b)

# fmod() / remainder()
x = 14
y = 3
z = math.fmod(x, y)
print(z)
# sqrt()
a = 16
b = math.sqrt(a)
print(b)
# divmod()
c = 16
d = 3
e = divmod(c, d)
print(e)
# exp()
f = 2
h = 3
g = math.exp(h)
print(g)
h = random.random()
print(h)
i = random.randrange(0, 10, 6)
print(i)
"""
j = datetime.now()
print(j)
m = datetime.time(j)
print(m.second)
k = date.today()
print(k)
print(k.weekday())
print(k.month)
y = 12
l = time()
print(l)

n = date.fromtimestamp(30194554)
print(n)
"""
@, upper 1, lower 1, 10 characters length min,
invalid password, create a new password
username no numbers, no special characters, space
invalid username, create a new username

enter date, then separate to yr, month, day
enter time, then separate to hr, min, sec
"""