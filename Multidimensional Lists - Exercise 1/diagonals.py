def read_matrix():
    n = int(input())
    mm = []

    for _ in range(n):
        mm.append([int(i) for i in input().split(', ')])

    return mm


def primary_diagonal(matrix):
    ll = []

    for i in range(len(matrix)):
        ll.append(matrix[i][i])

    return ll


def second_diagonal(matrix):
    sl = []

    for i in range(len(matrix)):
        sl.append(matrix[i][len(matrix) - 1 - i])

    return sl


matrix = read_matrix()
primary_diagonal = primary_diagonal(matrix)
secondary_diagonal = second_diagonal(matrix)
print(f'Primary diagonal: {", ".join(str(i) for i in primary_diagonal)}. Sum: {sum(primary_diagonal)}')
print(f'Secondary diagonal: {", ".join(str(i) for i in secondary_diagonal)}. Sum: {sum(secondary_diagonal)}')