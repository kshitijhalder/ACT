"""
Data Types - 
    -   int
    -   float
    -   complex
    -   bool
    -   str
    -   bytes
    -   bytearray
    -   range
    -   list
    -   tuple
    -   set
    -   frozenset
    -   dict
    -   None
    -   Ellipsis
    -   NotImplemented
    -   __debug__
Date : 7.3.2024
"""
import os

os.system('clear')
a = 5
b = 5.0
c= [1,2,3,4,5]
d = (1,2,3,4,5)
e = {1,2,3,4,5}
f = {1: 'one', 2: 'two', 3: 'three'}
g = "Hello"
h = b"Hello"
i = bytearray(10)
j = range(10)
k = True
l = False
m = complex(2,3)
n = None
o = ...
p = NotImplemented
q = __debug__
print("a is of type",type(a))
print("b is of type",type(b))
print("c is of type",type(c))
print("d is of type",type(d))
print("e is of type",type(e))
print("f is of type",type(f))
print("g is of type",type(g))
print("h is of type",type(h))
print("i is of type",type(i))
print("j is of type",type(j))
print("k is of type",type(k))
print("l is of type",type(l))
print("m is of type",type(m))
print("n is of type",type(n))
print("o is of type",type(o))
print("p is of type",type(p))
print("q is of type",type(q))