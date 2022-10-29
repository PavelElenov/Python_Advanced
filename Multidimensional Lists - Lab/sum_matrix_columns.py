def read_matrix():
    global m

    n, m = [int(x) for x in input().split(', ')]
    mm = []

    for _ in range(n):
        ll = [int(x) for x in input().split()]
        mm.append(ll)

    return mm


def sum_of_columns(some_matrix):
    for i in range(m):
        column_sum = 0
        for j in range(len(some_matrix)):
            column_sum += some_matrix[j][i]
        print(column_sum)


matrix = read_matrix()
sum_of_columns(matrix)
