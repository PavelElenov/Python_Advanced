string = input()
data = {}

for i in string:
    if i not in data:
        data[i] = string.count(i)

for key in sorted(data.items()):
    print(f"{key[0]}: {key[1]} time/s")
