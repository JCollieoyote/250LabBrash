''' Type your code here. '''
word_pairs = input().split()
contact_list = {}

for pair in word_pairs:
    name, phone = pair.split(',')
    contact_list[name] = phone

search_name = input()

print(contact_list[search_name])