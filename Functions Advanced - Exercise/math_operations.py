from collections import deque


def math_operations(*args, **kwargs):
    index = 1
    args = deque(args)
    while args:
        number = args.popleft()
        if index == 1:
            kwargs['a'] += number
        elif index == 2:
            kwargs['s'] -= number
        elif index == 3:
            if number != 0:
                kwargs['d'] /= number
        else:
            index = 1
            kwargs['m'] *= number
            continue
        index += 1

    ll = []
    sorted_dict = dict(sorted(kwargs.items(), key=lambda x: (-x[1], x[0])))
    for el in sorted_dict:
        ll.append(f"{el}: {sorted_dict[el]:.1f}")
    return '\n'.join(ll)


print(math_operations(6.0, a=0, s=0, d=5, m=0))
