''' Type your code here. '''
while True:
    user_input = input()
    words = user_input.split()

    if words[0] == 'quit':
        break

    word = words[0]
    number = words[1]

    sentence = f"Eating {number} {word} a day keeps you happy and healthy."
    print(sentence)