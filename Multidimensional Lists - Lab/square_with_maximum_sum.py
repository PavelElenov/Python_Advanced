def read_matrix():
    global row

    row, col = [int(x) for x in input().split(', ')]
    mm = []

    for _ in range(row):
        mm.append([int(x) for x in input().split(', ')])

    return mm


def square_with_max_sum(some_matrix):
    square = []
    max_sum = 0

    for i in range(row - 1):
        ll = []
        max_element_index = some_matrix[i].index(max(some_matrix[i]))

        if max_element_index + 1 <= len(some_matrix[i]) - 1:
            ll.append([some_matrix[i][max_element_index], some_matrix[i][max_element_index + 1]])
            ll.append([some_matrix[i + 1][max_element_index], some_matrix[i + 1][max_element_index + 1]])
        else:
            ll.append([some_matrix[i][max_element_index - 1], some_matrix[i][max_element_index]])
            ll.append([some_matrix[i + 1][max_element_index - 1], some_matrix[i + 1][max_element_index]])

        total_sum = sum(ll[0]) + sum(ll[1])

        if total_sum > max_sum:
            max_sum = total_sum
            square = ll.copy()

    for el in square:
        print(' '.join(str(x) for x in el))

    print(max_sum)


matrix = read_matrix()
square_with_max_sum(matrix)
