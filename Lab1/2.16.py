import math
''' Type your code here. '''
x = float(input())
y = float(input())
z = float(input())

expression1 = x ** z
expression2 = x ** (y ** z)
expression3 = abs(x - y)
expression4 = (x ** z) ** 0.5

print(f'{expression1:.2f} {expression2:.2f} {expression3:.2f} {expression4:.2f}')