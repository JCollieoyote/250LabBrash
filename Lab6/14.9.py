# TODO: Write recursive print_num_pattern() function
def print_num_pattern(n, m):
    if n < 0:
        print(n, end=" ")
        return
    print(n, end=" ")
    print_num_pattern(n - m, m)
    print(n, end=" ")

if __name__ == "__main__":
    num1 = int(input())
    num2 = int(input())
    print_num_pattern(num1, num2)