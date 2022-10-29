with open('./txt.files/numbers.txt') as file_read:
    sum = 0
    for num in file_read:
        sum += int(num)
    print(sum)
    file_read.close()