#Name: Working with Python Classes
#Author: Jacob Palmer
#Date: 16 MAR 24
#---------------------------------------------------------------------------------------------------------------------
#Pseudocode: Learn math for the methods in the class complex.
# Add the string for the inputs
# Use the real and imaginary template to complete the mathematics in the methods
# Double check mathematical computations for __truediv__, __mod__, and __str__
# Add a ZeroDivisionError for __truediv__
#---------------------------------------------------------------------------------------------------------------------
#Program Inputs: any two sets of two real numbers
#Program Outptus: 5 mathematical computation based on the 5 methods in the class complex
#----------------------------------------------------------------------------------------------------------------------

import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, no):
        real = self.real + no.real
        imaginary = self.imaginary + no.imaginary
        return Complex(real, imaginary)

    def __sub__(self, no):
        real = self.real - no.real
        imaginary = self.imaginary - no.imaginary    
        return Complex(real, imaginary)

    def __mul__(self, no):
        real = (self.real)*(no.real)
        imaginary = (self.imaginary)*(no.imaginary)
        return Complex(real, imaginary)

    def __truediv__(self, no):
        denom = (self.real**2 + no.real**2)
        if denom == 0:
            raise ZeroDivisionError
        real = (self.real * no.real + self.imaginary * no.imaginary) / denom
        imaginary = (self.imaginary * no.real - self.real * no.imaginary) / denom
        return Complex(real, imaginary)

    def mod(self):
        real = math.sqrt((self.real**2) + (self.imaginary**2))
        return Complex(real, 0)

    def __str__(self):
        return f'{str(self.real)} + {str(self.imaginary)}i'

def num_inputs():
    C = map(float, input("enter two numbers: ").split())
    D = map(float, input("enter two numbers: ").split())
    x = Complex(*C)
    y = Complex(*D)
    print ('\n'.join(map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]))) 

num_inputs()