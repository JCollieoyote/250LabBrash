''' Type your code here. '''
name = input()


name_parts = name.split()

# Check if middle name is present
if len(name_parts) == 3:
    first_name, middle_name, last_name = name_parts
    initials = f"{first_name[0].upper()}.{middle_name[0].upper()}."
else:
    first_name, last_name = name_parts
    initials = f"{first_name[0].upper()}."

formatted_name = f"{last_name}, {initials}"
print(formatted_name)