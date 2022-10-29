numbers = tuple(float(i) for i in input().split())
unique_numbers = set()
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.add(num)
        print(f"{num:.1f} - {numbers.count(num)} times")
