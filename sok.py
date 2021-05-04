from sys import stdin

A, B, C = list(map(int, stdin.readline().split()))
I, J, K = list(map(int, stdin.readline().split()))

n = min(A / I, B / J, C / K)

print(A - I * n, B - J * n, C - K * n)
