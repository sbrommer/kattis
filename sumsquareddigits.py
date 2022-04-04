from sys import stdin

def readints():
    return list(map(int, stdin.readline().split()))

def SSD(b, n):
    aa = to_base_b(b, n)
    return sum(map(lambda a: a**2, aa))

def to_base_b(b, n):
    aa = []
    while n != 0:
        aa.append(n % b)
        n //= b
    return aa

p = int(stdin.readline())

for _ in range(p):
    K, b, n = readints()
    print(K, SSD(b, n))