def swap_values(user_val1, user_val2, user_val3, user_val4):
    return user_val2, user_val1, user_val4, user_val3

if __name__ == '__main__': 
    user_val1 = int(input())
    user_val2 = int(input())
    user_val3 = int(input())
    user_val4 = int(input())

    swapped_val1, swapped_val2, swapped_val3, swapped_val4 = swap_values(user_val1, user_val2, user_val3, user_val4)

    print(swapped_val1, swapped_val2, swapped_val3, swapped_val4)