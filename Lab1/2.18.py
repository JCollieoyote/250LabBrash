''' Type your code here. '''
nickels = int(input())
dimes = int(input())
quarters = int(input())

total_amount = nickels * 0.05 + dimes * 0.10 + quarters * 0.25

print(f'Amount: ${total_amount:.2f}')