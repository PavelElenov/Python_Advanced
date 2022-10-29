numbers = [x for x in input().split('|')]
matrix = []

for i in reversed(numbers):
    ll = i.strip().split()
    matrix.extend(ll)

print(' '.join(matrix))

