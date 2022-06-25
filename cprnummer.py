from operator import mul

ddmmyy, kkkk = input().split('-')

cpr = map(int, ddmmyy + kkkk)

check = [4, 3, 2, 7, 6, 5, 4, 3, 2, 1]

s = sum(map(mul, cpr, check))

print(int(not s % 11))
