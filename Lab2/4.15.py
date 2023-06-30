highway_number = int(input())

''' Type your code here. '''
if highway_number >= 1 and highway_number <= 99:
    direction = "north/south" if highway_number % 2 != 0 else "east/west"
    print(f"I-{highway_number} is primary, going {direction}.")
elif highway_number >= 100 and highway_number <= 999:
    primary_highway = highway_number % 100
    if primary_highway == 0:
        print(f"{highway_number} is not a valid interstate highway number.")
    else:
        direction = "north/south" if primary_highway % 2 != 0 else "east/west"
        print(f"I-{highway_number} is auxiliary, serving I-{primary_highway}, going {direction}.")
else:
    print(f"{highway_number} is not a valid interstate highway number.")