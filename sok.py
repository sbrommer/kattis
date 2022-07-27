A, B, C = map(int, input().split())
I, J, K = map(int, input().split())

n = min(A / I, B / J, C / K)

print(A - I * n, B - J * n, C - K * n)
