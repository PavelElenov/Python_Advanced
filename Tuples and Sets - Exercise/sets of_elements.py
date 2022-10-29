n, m = input().split()
numbers = list()
unique_numbers = set()
for i in range(int(n)):
    number = int(input())
    numbers.append(number)

for j in range(int(m)):
    number = int(input())
    if number in numbers:
        unique_numbers.add(number)

print('\n'.join(str(i) for i in unique_numbers))
