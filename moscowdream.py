from sys import stdin

a, b, c, n = list(map(int, stdin.readline().split()))

print('YES' if a and b and c and a + b + c >= n >= 3 else 'NO')
