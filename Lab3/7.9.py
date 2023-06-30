''' Type your code here. '''
user_input = input()

input_no_spaces = user_input.replace(" ", "").lower()

if input_no_spaces == input_no_spaces[::-1]:
    print("palindrome:", user_input)
else:
    print("not a palindrome:", user_input)