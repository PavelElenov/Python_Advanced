n = int(input())
cars = set()

for i in range(n):
    direction, car_number = input().split(', ')

    if direction == 'IN':
        cars.add(car_number)
    else:
        if car_number in cars:
            cars.remove(car_number)

if len(cars) > 0:
    print('\n'.join(car for car in cars))
else:
    print("Parking Lot is Empty")
