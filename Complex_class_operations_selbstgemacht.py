# -*- coding: utf-8 -*-
"""
Created on Monday Dec  6 14:30 2021

@author: Ricardo
"""

import math
c = map(float, input().split())
d = map(float, input().split())


class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, no):
        a = self.real+no.real
        b = self.imaginary+no.imaginary
        return Complex(a, b)

    def __sub__(self, no):
        a = self.real-no.real
        b = self.imaginary-no.imaginary
        return Complex(a, b)

    def __mul__(self, no):
        a = self.real*no.real-self.imaginary*no.imaginary
        b = self.real*no.imaginary+no.real*self.imaginary
        return Complex(a, b)

    def __truediv__(self, no):
        a = (self.real*no.real+self.imaginary*no.imaginary)/(no.mod().real**2)
        b = (no.real*self.imaginary-self.real*no.imaginary)/(no.mod().real**2)
        return Complex(a, b)

    def mod(self):
        return Complex((self.real**2+self.imaginary**2)**0.5, 0)

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result


x = Complex(*c)
y = Complex(*d)

print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x.mod())
print(y.mod())
