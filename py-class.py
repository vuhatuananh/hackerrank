#py-class.py
#author: Tuan Anh Vu

#https://www.hackerrank.com/challenges/class-1-dealing-with-complex-numbers
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
        real = self.real*no.real - self.imaginary*no.imaginary 
        imaginary = self.real*no.imaginary + self.imaginary*no.real 
        return Complex(real, imaginary)

    def __truediv__(self, no):
        real = (self.real*no.real + self.imaginary*no.imaginary) / (no.real**2 + no.imaginary**2) 
        imaginary = (self.imaginary*no.real - self.real*no.imaginary) / (no.real**2 + no.imaginary**2) 
        return Complex(real, imaginary)

    def mod(self):
        real = math.sqrt(self.real**2 + self.imaginary**2)
        return Complex(real, 0)

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

if __name__ == '__main__':

#https://www.hackerrank.com/challenges/class-2-find-the-torsional-angle
import math

class Points(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, no):
        i = self.x - no.x
        j = self.y - no.y
        k = self.z - no.z
        return Points(i,j,k)
    def dot(self, no):
        return self.x*no.x + self.y*no.y + self.z*no.z

    def cross(self, no):
        i = self.y * no.z - self.z * no.y
        j = self.x * no.z - self.z * no.x
        k = self.x * no.y - self.y * no.x
        return Points(i,j,k)
        
    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)

if __name__ == '__main__':


#
#
#
#
#
