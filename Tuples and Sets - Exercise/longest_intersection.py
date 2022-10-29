def add(start_index, end_index):
    some_list = []

    for el in range(start_index, end_index + 1):
        some_list.append(el)

    return some_list


n = int(input())
intersections = []

for i in range(n):
    intersection = []
    start = 0
    end = 0
    first_seq, second_seq = input().split('-')
    first_start, first_end = [int(i) for i in first_seq.split(',')]
    second_start, second_end = [int(i) for i in second_seq.split(',')]

    if int(second_end) > int(first_end):
        end = int(first_end)
    else:
        end = int(second_end)

    if int(first_start) > int(second_start):
        start = int(first_start)
    else:
        start = int(second_start)

    intersection = add(start, end)
    intersections.append(intersection)

intersections = sorted(intersections, key=lambda x: len(x), reverse=True)
max_intersection = intersections[0]
print(f"Longest intersection is {max_intersection} with length {len(max_intersection)}")




