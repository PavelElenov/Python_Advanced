n = int(input())
reservation_numbers = set()

for i in range(n):
    reservation_number = input()
    reservation_numbers.add(reservation_number)

while True:
    command = input()

    if command == 'END':
        break

    if command in reservation_numbers:
        reservation_numbers.remove(command)

print(len(reservation_numbers))
print('\n'.join(i for i in sorted(reservation_numbers)))
