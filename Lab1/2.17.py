''' Type your code here. '''
import math

f_0 = float(input())

r = pow(2, 1/12)
f_1 = f_0 * pow(r, 1)
f_2 = f_0 * pow(r, 2)
f_3 = f_0 * pow(r, 3)

print(f'{f_0:.2f} Hz')
print(f'{f_1:.2f} Hz')
print(f'{f_2:.2f} Hz')
print(f'{f_3:.2f} Hz')