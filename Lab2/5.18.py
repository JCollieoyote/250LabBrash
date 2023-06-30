''' Read in first equation, ax + by = c '''
a = int(input())
b = int(input())
c = int(input())

''' Read in second equation, dx + ey = f '''
d = int(input())
e = int(input())
f = int(input())

''' Type your code here. '''
solution_found = False

# Loop through all possible values of x and y in the range -10 to 10
for x in range(-10, 11):
    for y in range(-10, 11):
        # Check if the current x and y satisfy both equations
        if a * x + b * y == c and d * x + e * y == f:
            # Output the solution and set the flag to indicate a solution was found
            print(f'x = {x} , y = {y}')
            solution_found = True
            break

# If no solution was found, print the appropriate message
if not solution_found:
    print('There is no solution')