from collections import deque

dispenser_liters = int(input())
queue = deque()

while True:
    command = input()

    if command == "Start":
        break

    name = command
    queue.append(name)

while True:
    command = input()

    if command == 'End':
        break

    if command.isdigit():
        if dispenser_liters >= int(command):
            print(f"{queue.popleft()} got water")
            dispenser_liters -= int(command)
        else:
            print(f"{queue.popleft()} must wait")
    else:
        command = command.split()
        dispenser_liters += int(command[1])

print(f'{dispenser_liters} liters left')