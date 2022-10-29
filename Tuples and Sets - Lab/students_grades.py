from collections import defaultdict

n = int(input())
data = defaultdict(list)

for i in range(n):
    students_info = input().split()
    data[students_info[0]].append(float(students_info[1]))

for data in data.items():
    # print(f'{student} -> {" ".join(f"{i:.2f}" for i in grades)} (avg: {sum(grades) / len(grades):.2f})')
    """data is tuple with two arguments(first is name, second is list with grades)"""
    print(f"{data[0]} -> {' '.join(f'{i:.2f}' for i in data[1])} (avg: {sum(data[1]) / len(data[1]):.2f})")
