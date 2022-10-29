from collections import defaultdict


def start_spring(**kwargs):
    data = defaultdict(list)
    for key, value in kwargs.items():
        data[value].append(key)

    data = dict(sorted(data.items(), key=lambda x: (-len(x[1]), x[0])))
    ll = []
    for key, value in data.items():
        ll.append(f'{key}:')
        for item in sorted(value):
            ll.append(f"-{item}")
    return '\n'.join(ll)





