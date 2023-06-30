phone_number = int(input())

''' Type your code here. '''

area_code = phone_number // 10000000
prefix = (phone_number // 10000) % 1000
line_number = phone_number % 10000

formatted_number = f"({area_code}) {prefix}-{line_number}"
print(formatted_number)