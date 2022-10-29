def read_even_numbers_matrix():
    n = int(input())
    mm = []

    for _ in range(n):
        ll = [int(x) for x in input().split(', ') if int(x) % 2 == 0]
        mm.append(ll)

    return mm


matrix = read_even_numbers_matrix()
print(matrix)

