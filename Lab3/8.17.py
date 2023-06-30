''' Type your code here. '''
numbers = input().split()

numbers = [int(num) for num in numbers]

negative_numbers = sorted(filter(lambda x: x < 0, numbers), reverse=True)

output = ' '.join(map(str, negative_numbers))
print(output, end=' ')