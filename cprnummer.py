ddmmyy, kkkk  = open(0).readline().strip().split('-')

cpr = [int(c) for c in ddmmyy + kkkk]

check = [4, 3, 2, 7, 6, 5, 4, 3, 2, 1]

s = sum(n * m for (n, m) in zip(cpr, check))

print(int(not s % 11))
