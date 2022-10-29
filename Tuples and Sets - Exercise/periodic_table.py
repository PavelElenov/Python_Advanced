n = int(input())
unique_chemicals = set()

for i in range(n):
    chemicals = input().split()

    for el in chemicals:
        unique_chemicals.add(el)

print('\n'.join(unique_chemicals))  
