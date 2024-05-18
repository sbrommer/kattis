from itertools import accumulate

N = int(input())
cs = [int(n) for n in input().split()]

acc = [*accumulate(cs)]

n_students = acc[-1]
n_bus = n_students // 3

if all(n_bus * i in acc for i in [1, 2, 3]):
    print(acc.index(n_bus) + 1, acc.index(n_bus * 2) + 1)
else:
    print(-1)
