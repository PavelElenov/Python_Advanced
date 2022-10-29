'''
aaa aba aca ada aea afa
bbb bcb bdb beb bfb bgb
ccc cdc cec cfc cgc chc
ddd ded dfd dgd dhd did

i = 0
j = 0
result = "aaa"
result[0] = chr(97 + i)
result[2] = result[0]
result[1] = chr(97 + j)
97 + i =
'''

rows, cols = [int(x) for x in input().split()]
matrix = []

for i in range(rows):
    string = chr(97 + i) * 3
    ll = []

    for j in range(cols):
        new_string = string[0] + chr(97 + j + i) + string[2]
        ll.append(new_string)

    matrix.append(ll)

for el in matrix:
    print(' '.join(str(x) for x in el))
