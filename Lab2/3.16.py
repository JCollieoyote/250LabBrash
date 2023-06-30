num1 = float(input())
num2 = float(input())
num3 = float(input())
num4 = float(input())

''' Type your code here. '''
product = num1 * num2 * num3 * num4
average = (num1 + num2 + num3 + num4) / 4

rounded_product = int(round(product))
rounded_average = int(round(average))

float_product = round(product, 3)
float_average = round(average, 3)

print(f'{rounded_product} {rounded_average}')
print(f'{float_product:.3f} {float_average:.3f}')