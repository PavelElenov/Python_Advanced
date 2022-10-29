def add_songs(*args):
    data = {}
    result = []

    for item in args:
        title = item[0]
        list_of_songs = item[1]

        if title not in data:
            data[title] = []

        if list_of_songs:
            for song in list_of_songs:
                data[title].append(song)

    for song_title in data:
        result.append(f'- {song_title}')
        songs = data[song_title]

        for song in songs:
            result.append(song)

    return '\n'.join(result)


print(add_songs(
    ("Beat It", []),
    ("Beat It",
     ["Just beat it (beat it), beat it (beat it)",
      "No one wants to be defeated"]),
    ("Beat It", []),
    ("Beat It",
     ["Showin' how funky and strong is your fight",
      "It doesn't matter who's wrong or right"]),
))

