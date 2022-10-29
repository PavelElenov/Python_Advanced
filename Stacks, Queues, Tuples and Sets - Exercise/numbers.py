def remove(some_numbers, some_sequence):
    for num in some_numbers:
        if num in some_sequence:
            some_sequence.remove(num)

    return some_sequence


def check_subset(seq_1, seq_2):
    for num in seq_1:
        if num not in seq_2:
            return False

    return True


first_sequence = set(int(i) for i in input().split())
second_sequence = set(int(i) for i in input().split())
n = int(input())


for _ in range(n):
    command = input()
    command = command.split()
    numbers = set()

    if command[0] == 'Add':
        for index in range(2, len(command)):
            numbers.add(int(command[index]))

        if command[1] == "First":
            first_sequence = first_sequence | numbers
        else:
            second_sequence = second_sequence | numbers
    elif command[0] == 'Remove':
        for index in range(2, len(command)):
            numbers.add(int(command[index]))

        if command[1] == 'First':
            first_sequence = remove(numbers, first_sequence)
        else:
            second_sequence = remove(numbers, second_sequence)
    else:
        if len(first_sequence) < len(second_sequence):
            print(check_subset(first_sequence, second_sequence))
        else:
            print(check_subset(second_sequence, first_sequence))

print(', '.join(str(num) for num in sorted(first_sequence)))
print(', '.join(str(num) for num in sorted(second_sequence)))