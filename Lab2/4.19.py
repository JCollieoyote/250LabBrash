''' Type your code here. '''
par = int(input())
score = int(input())

if par < 3 or par > 5 or score < 1 or score > 10:
    print("Error")
else:
    strokes_difference = score - par

    if strokes_difference == -2:
        print("Eagle")
    elif strokes_difference == -1:
        print("Birdie")
    elif strokes_difference == 0:
        print("Par")
    elif strokes_difference == 1:
        print("Bogey")
    else:
        print("Error")