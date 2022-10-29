def even_odd(*args):
    def even():
        even_numbers = []
        for num in args[:len(args) - 1]:
            if num % 2 == 0:
                even_numbers.append(num)
        return even_numbers

    def odd():
        odd_numbers = []
        for num in args[:len(args) - 1]:
            if num % 2 != 0:
                odd_numbers.append(num)
        return odd_numbers

    if args[-1] == 'even':
        return even()
    else:
        return odd()


print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
