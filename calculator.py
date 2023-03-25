import math

class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self, a, b):
        sum = a + b
        print('----------------------------------------------------------')
        print(sum)
        print('----------------------------------------------------------')

    def subtration(self, a, b):
        difference = a - b
        print('----------------------------------------------------------')
        print(difference)
        print('----------------------------------------------------------')

    def division(self, a, b):
        divide = a // b
        print('----------------------------------------------------------')
        print(divide)
        print('----------------------------------------------------------')

    def multiplication(self, a, b):
        product = a * b
        print('----------------------------------------------------------')
        print(product)
        print('----------------------------------------------------------')

    def logarithms(self, a, b):
        print('----------------------------------------------------------')
        print(math.log10(a))
        print(math.log10(b))
        print('----------------------------------------------------------')

    # def sine(self, a, b = None):
    #     print('----------------------------------------------------------')
    #     print(math.sin(a))
    #     print(math.sin(b))
    #     print('----------------------------------------------------------')

    def binary(self, a, b = None):
        print('----------------------------------------------------------')
        c = bin(a)
        d = bin(b)
        print(c)
        print(d)
        print('----------------------------------------------------------')

    def hexadecimal(self, a, b = None):
        print('----------------------------------------------------------')
        e = hex(a)
        f = hex(b)
        print(e)
        print(f)
        print('----------------------------------------------------------')

    def octaldecimal(self, a, b = None):
        print('----------------------------------------------------------')
        g = oct(a)
        h = oct(b)
        print(g)
        print(h)
        print('----------------------------------------------------------')

    def absolute_value(self, a, b = None):
        print('----------------------------------------------------------')
        i = abs(a)
        j = abs(b)
        print(i)
        print(j)
        print('----------------------------------------------------------')






a = int(input("enter value -- "))
b = int(input("enter value -- "))
operation = Calculator(a, b)
# operation.addition(a,b)
# operation.subtration(a,b)
# operation.multiplication(a,b)
operation.logarithms(a, b)
# operation.binary(a,b)
# operation.hexadecimal(a,b)
# operation.octaldecimal(a,b)
# operation.absolute_value(a,b)








