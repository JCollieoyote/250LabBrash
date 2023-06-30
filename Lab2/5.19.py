''' Type your code here. '''
n = int(input())  # Read the number of floating-point values

# Read the floating-point values and store them in a list
values = []
for _ in range(n):
    value = float(input())
    values.append(value)

# Find the largest value in the list
max_value = max(values)

# Adjust and print each value divided by the largest value
for value in values:
    adjusted_value = value / max_value
    print(f'{adjusted_value:.2f}')