"""Numerical Operators Exercise"""

__author__ = 730364448

left: str = input("Left-hand side: ")
right: str = input("Right-hand side ")
print(left + " < " + right + " is " + str(bool(int(left)<int(right))))
print(left + " >= " + right + " is " + str(bool(int(left)>=int(right))))
print(left + " == " + right + " is " + str(bool(int(left)==int(right))))
print(left + " != " + right + " is " + str(bool(int(left)!=int(right))))