from collections import deque


def shopping_cart(*args):
    args = deque(args)
    data = {'Pizza': [], 'Soup': [], 'Dessert': []}
    ll = []
    while args:
        product_info = args.popleft()
        if product_info == 'Stop':
            break

        meal, product = product_info

        add = False
        if product not in data[meal]:
            if meal == 'Pizza':
                if len(data[meal]) < 4:
                    add = True
            elif meal == 'Dessert':
                if len(data[meal]) < 2:
                    add = True
            else:
                if len(data[meal]) < 3:
                    add = True

            if add:
                data[meal].append(product)

    if len(data['Pizza']) == 0 and len(data['Dessert']) == 0 and len(data['Soup']) == 0:
        ll.append('No products in the cart!')
    else:
        data = dict(sorted(data.items(), key=lambda x: (-len(x[1]), x[0])))
        for v in data:
            ll.append(f'{v}:')
            for el in sorted(data[v]):
                ll.append(f' - {el}')
    return '\n'.join(str(x) for x in ll)