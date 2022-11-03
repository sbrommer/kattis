d_list = [int(input()) for _ in range(9)]

d_set = set(d_list)

n = sum(d_set) - 100

for d1 in d_list:
    d2 = n - d1
    if d1 == d2 or d2 not in d_set:
        print(d1)
