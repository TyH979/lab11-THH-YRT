# https://github.com/TyH979/lab11-THH-YRT
# Partner 1: Ty Holmgren
# Partner 2: Yoav Tsadok
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math
# First example
def add(a, b): 
    return a+b
def subtract(a, b):
    return a-b
def multiply(a, b):
    return a*b
def divide(a, b):
    if a == 0:
        raise ValueError("Cannot divide by zero")
    return b/a
def logarithm(a, b):
    if a <= 0 or b <= 0 or a == 1:
        raise ValueError("Invalid logarithm")
    return math.log(b, a)
def exponent(a, b):
    return a**b

