''' Type your code here. '''
input_str = input()

character, phrase = input_str.split(' ', 1)

count = phrase.count(character)

plural = "'s" if count != 1 else ''

output = f"{count} {character}{plural}"
print(output)