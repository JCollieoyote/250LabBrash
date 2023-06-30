''' Type your code here. '''
mileage = float(input())
cost_per_gallon = float(input())

distance1 = 20
distance2 = 75
distance3 = 500

gas_cost1 = (distance1 / mileage) * cost_per_gallon
gas_cost2 = (distance2 / mileage) * cost_per_gallon
gas_cost3 = (distance3 / mileage) * cost_per_gallon

print(f'{gas_cost1:.2f} {gas_cost2:.2f} {gas_cost3:.2f}')