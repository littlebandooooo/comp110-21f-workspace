"""Numerical Operators Exercise"""

__author__ = 730364448 

first: str = input("Left-hand side: ")
second: str = input("Right-hand side: ")
x = int(second)
y = int(first)
print(first + " ** " + second + " is " + str(x ** y))
print(first + " / " + second + " is " + str(x / y))
print(first + " // " + second + " is " +  str(x // y))
print(first + " % " + second + " is " + str(x % y))