o = open(0)

t = int(o.readline())

d = {(n * 7 % 10): n for n in range(1, 11)}

for _ in range(t):
    N = int(o.readline())

    n = d[N % 10]

    print(n if N >= n * 7 else -1)
