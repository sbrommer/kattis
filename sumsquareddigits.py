def readints():
    return map(int, input().split())


def SSD(b, n):
    return sum(map(lambda a: a ** 2, to_base_b(b, n)))


def to_base_b(b, n):
    aa = []
    while n:
        n, a = divmod(n, b)
        aa.append(a)
    return aa


P = int(input())

for _ in range(P):
    K, b, n = readints()
    print(K, SSD(b, n))
