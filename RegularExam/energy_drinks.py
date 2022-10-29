from collections import deque

milligrams_of_caffeine = [int(x) for x in input().split(', ')]
energy_drinks = deque(int(x) for x in input().split(', '))
stamat_caffeine = 0

while milligrams_of_caffeine and energy_drinks:
    milligram_coffeine = milligrams_of_caffeine.pop()
    energy_drink = energy_drinks.popleft()

    caffeine_in_the_drink = milligram_coffeine * energy_drink

    if caffeine_in_the_drink + stamat_caffeine <= 300:
        stamat_caffeine += caffeine_in_the_drink
    else:
        stamat_caffeine -= 30
        if stamat_caffeine < 30:
            stamat_caffeine = 0
        energy_drinks.append(energy_drink)


if energy_drinks:
    print(f"Drinks left: {', '.join(str(x) for x in energy_drinks)}")

else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with { stamat_caffeine } mg caffeine.")


