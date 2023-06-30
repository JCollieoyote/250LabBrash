user_string = input()

''' Type your code here. '''
def is_integer_string(input_str):
    for char in input_str:
        if not char.isdigit():
            return "No"
    return "Yes"

result = is_integer_string(user_string)
print(result)