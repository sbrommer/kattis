n, c, p = map(int, input().split())

n_records = 0

for _ in range(n):
    height = int(input())

    if height > c + p:
        c, p = height, c
        n_records += 1

print(n_records)
