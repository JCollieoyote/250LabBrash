''' Type your code here. '''
numbers = input().split()
numbers = [int(num) for num in numbers]

lower_bound, upper_bound = input().split()
lower_bound = int(lower_bound)
upper_bound = int(upper_bound)

output_numbers = [num for num in numbers if lower_bound <= num <= upper_bound]

output = ','.join(map(str, output_numbers))
print(output, end=',')