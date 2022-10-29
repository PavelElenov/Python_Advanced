def read_list():
    n = int(input())
    list = []

    for _ in range(n):
        ll = [int(x) for x in input().split(', ')]

        for el in ll:
            list.append(el)

    return list


numbers = read_list()
print(numbers)
