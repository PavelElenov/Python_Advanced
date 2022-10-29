from collections import deque, defaultdict

materials_values = [int(i) for i in input().split()]
magic_values = deque(int(i) for i in input().split())

magic_needed = [150, 250, 300, 400]
crafts = defaultdict(int)
crafted = False

while materials_values and magic_values:
    material = materials_values.pop()
    magic_level = magic_values.popleft()

    if material == 0 and magic_level == 0:
        continue
    if material == 0:
        magic_values.appendleft(magic_level)
        continue
    if magic_level == 0:
        materials_values.append(material)
        continue

    result = material * magic_level

    if result in magic_needed:
        if result == 150:
            crafts['Doll'] += 1
        elif result == 250:
            crafts['Wooden train'] += 1
        elif result == 300:
            crafts['Teddy bear'] += 1
        else:
            crafts['Bicycle'] += 1
    elif result < 0:
        result = abs(material + magic_level)
        materials_values.append(result)
    else:
        materials_values.append(material + 15)

if 'Doll' in crafts and 'Wooden train' in crafts:
    crafted = True
elif 'Teddy bear' in crafts and 'Bicycle' in crafts:
    crafted = True

if crafted:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials_values:
    print(f'Materials left: {", ".join(str(el) for el in reversed(materials_values))}')
if magic_values:
    print(f"Magic left: {', '.join(str(i) for i in magic_values)}")

for el in sorted(crafts):
    print(f"{el}: {crafts[el]}")



