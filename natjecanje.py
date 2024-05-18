def readints():
    return [int(n) for n in input().split()]


N, *_ = readints()
Ss = set(readints())
Rs = set(readints())

solved = set.intersection(Ss, Rs)
Ss -= solved
Rs -= solved

for n in range(1, N + 1):
    if n in Ss:
        if n - 1 in Rs:
            Rs.remove(n - 1)
            Ss.remove(n)
        elif n + 1 in Rs:
            Rs.remove(n + 1)
            Ss.remove(n)

print(len(Ss))
