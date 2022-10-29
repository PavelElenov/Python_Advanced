from collections import deque

duration_of_green_light = int(input())
duration_of_free_windows = int(input())
cars_queue = deque()
count = 0

while True:
    command = input()
    green_light_time = duration_of_green_light
    free_windows_time = duration_of_free_windows
    if command == 'END':
        break
    elif command == 'green':
        while cars_queue:
            crashed = False
            for letter in cars_queue[0]:
                green_light_time -= 1
                if green_light_time < 0:
                    free_windows_time -= 1
                    if free_windows_time < 0:
                        print('A crash happened!')
                        print(f"{cars_queue.popleft()} was hit at {letter}.")
                        crashed = True
                        break
            else:
                cars_queue.popleft()
                count += 1
                if green_light_time <= 0:
                    break
            if crashed:
                exit()
    else:
        cars_queue.append(command)

print('Everyone is safe.')
print(f"{count} total cars passed the crossroads.")


