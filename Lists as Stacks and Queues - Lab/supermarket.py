from collections import deque

queue = deque()

while True:
    command = input()

    if command == 'End':
        break

    if command == 'Paid':
        for i in range(len(queue)):
            print(queue.popleft())
    else:
        queue.append(command)

print(f"{len(queue)} people remaining.")
