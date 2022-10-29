number = tuple(int(i) for i in input().split())
target_number = int(input())
iteration = 0
unique_pairs = set()

for i in range(len(number) - 1):
    for j in range(i + 1, len(number)):
        iteration += 1
        if number[i] + number[j] == target_number:
            print(f"{number[i]} + {number[j]} = {target_number}")
            unique_pairs.add((number[i], number[j]))

print(f'Iterations done: {iteration}')
print('\n'.join(str(_) for _ in unique_pairs))