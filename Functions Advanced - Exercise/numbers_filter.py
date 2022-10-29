def even_odd_filter(**kwargs):
    dictionary = {}

    def even(value):
        ll = []
        for el in value:
            if el % 2 == 0:
                ll.append(el)
        return ll

    def odd(value):
        ll = []
        for el in value:
            if el % 2 != 0:
                ll.append(el)
        return ll

    for key, value in kwargs.items():
        if key == 'even':
            even_numbers = even(value)
            dictionary[key] = even_numbers
        else:
            odd_numbers = odd(value)
            dictionary[key] = odd_numbers
    return dict(sorted(dictionary.items(), key=lambda x: len(x[1]), reverse=True))


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))
