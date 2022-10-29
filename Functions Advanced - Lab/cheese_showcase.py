def sorting_cheeses(**kwargs):
    sorted_dict = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))
    result = []

    for name, pieces in sorted_dict:
        result.append(name)
        result.extend(sorted(pieces, reverse=True))

    return '\n'.join([str(z) for z in result])


print(
    sorting_cheeses(
        Parmigiano=[165, 215],
        Feta=[150, 515],
        Brie=[150, 125]
    )
)

