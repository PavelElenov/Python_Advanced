def read_matrix():
    n, m = [int(x) for x in input().split(', ')]
    matrix = []

    for _ in range(n):
        ll = [int(el) for el in input().split(', ')]
        matrix.append(ll)

    return matrix


def sum_matrix(some_matrix):
    sum_of_all_elements = 0

    for i in range(len(matrix)):
        sum_of_all_elements += sum(matrix[i])

    return sum_of_all_elements


matrix = read_matrix()
total_sum = sum_matrix(matrix)
print(total_sum)
print(matrix)