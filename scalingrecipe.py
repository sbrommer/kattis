o = open(0)

n, x, y = [int(n) for n in o.readline().split()]

for _ in range(n):
    a = int(o.readline())
    print(int(a / x * y))
