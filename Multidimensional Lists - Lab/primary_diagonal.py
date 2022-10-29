'''
1 2 4 1 1 --0
4 5 6 1 1 -- 1
1 8 -1 1 2-- 2

for i in range(len(mm)) #0
    diagonal_sum += mm[i][i]
'''

n = int(input())
mm = []

for i in range(n):
    ll = [int(x) for x in input().split()]
    mm.append(ll)

diagonal_sum = 0

for j in range(n):
    diagonal_sum += mm[j][j]

print(diagonal_sum)
