from collections import deque
from time import strftime
from time import gmtime


def time_to_seconds(param):
    param = param.split(':')
    return int(param[0]) * 60 * 60 + int(param[1]) * 60 + int(param[2])


data = input().split(';')
robots_info = {}

for i in data:
    i = i.split('-')
    robots_info[i[0]] = int(i[1])

time = time_to_seconds(input())
robots_time_working = {}

for element in robots_info:
    robots_time_working[element] = time

products = deque()

while True:
    command = input()

    if command == 'End':
        break

    products.append(command)

while products:
    time += 1
    for robot in robots_time_working:
        if time >= robots_time_working[robot]:
            robots_time_working[robot] = time + robots_info[robot]
            print(f"{robot} - {products.popleft()} [{strftime('%H:%M:%S', gmtime(time))}]")
            break
    else:
        products.rotate(-1)





