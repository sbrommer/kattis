from sys import stdin

def hailstone_sum(n):
    if n == 1:
        return n

    else:
        m = n * 3 + 1 if n % 2 else n // 2
        return n + hailstone_sum(m)

n = int(stdin.readline())
print(hailstone_sum(n))

