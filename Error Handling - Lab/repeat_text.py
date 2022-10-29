try:
    text = input()
    time = int(input())
    print(text * time)
except ValueError:
    print('Time must be integer!')