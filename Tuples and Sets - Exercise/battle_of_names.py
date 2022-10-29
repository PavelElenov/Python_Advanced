def sum_the_ascii_values(some_name: str, integer: int):
    sum = 0
    for letter in some_name:
        sum += ord(letter)

    sum //= integer
    return sum


n = int(input())
even = set()
odd = set()
sum_of_letters = 0

for i in range(1, n + 1):
    names = input()
    sum_of_letters = sum_the_ascii_values(names, i)

    if sum_of_letters % 2 == 0:
        even.add(sum_of_letters)
    else:
        odd.add(sum_of_letters)

if sum(even) > sum(odd):
    total_set = even | odd
    print(', '.join(str(i) for i in total_set))
elif sum(even) < sum(odd):
    print(', '.join(str(i) for i in odd))
else:
    total_set = odd | even
    print(', '.join(str(el) for el in total_set))
