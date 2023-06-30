def fibonacci(n):
    if n < 0:
        return -1
    elif n == 0:
        return 0
    elif n == 1:
        return 1

    fib_n_minus_2 = 0
    fib_n_minus_1 = 1

    for _ in range(2, n + 1):
        fib_n = fib_n_minus_1 + fib_n_minus_2
        fib_n_minus_2 = fib_n_minus_1
        fib_n_minus_1 = fib_n

    return fib_n


if __name__ == '__main__':
    start_num = int(input())
    print(f'fibonacci({start_num}) is {fibonacci(start_num)}')