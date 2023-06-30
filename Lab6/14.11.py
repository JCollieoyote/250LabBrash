# TODO: Write recursive draw_triangle() function here.
def draw_triangle(base_length):
    if base_length == 1:
        print("         *")
    else:
        draw_triangle(base_length - 2)
        print(" " * ((19 - base_length) // 2) + "*" * base_length)

if __name__ == '__main__':
    base_length = int(input())
    draw_triangle(base_length)