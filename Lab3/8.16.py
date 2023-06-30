''' Type your code here. '''
numbers = input().split()

numbers = [float(num) for num in numbers]
maximum = max(numbers)

average = sum(numbers) / len(numbers)

print(f"{maximum:.2f} {average:.2f}")