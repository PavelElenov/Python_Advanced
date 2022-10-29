def print_triangle(size):
    def line(size):
        for j in range(1, size + 1):
            print(j, end=" ")
        print()

    for i in range(1, size + 1):
        line(i)
    for k in range(size - 1, 0, -1):
        line(k)