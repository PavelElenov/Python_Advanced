with open('./txt.files/words.txt') as file:
    words = file.readline().split()
    for word in words:
        word_count = 0
        with open('./txt.files/input.txt') as file2:
            lines = file2.readlines()
            for line in lines:
                word_count += line.count(word)
            file2.close()
        with open('./txt.files/output.txt', 'a') as output_file:
            output_file.write(f"{word} - {word_count}\n")
            output_file.close()
    file.close()

with open('./txt.files/output.txt') as read_file:
    dd = {}
    for line in read_file:
        key, value = line.split(' - ')
        dd[key] = int(value.strip())
    sorted_dd = dict(sorted(dd.items(), key=lambda x: -x[1]))

    for el in sorted_dd:
        print(f"{el} - {sorted_dd[el]}")



