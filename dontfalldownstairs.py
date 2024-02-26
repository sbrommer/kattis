input()

A = [int(n) for n in input().split()] + [0]

print(sum([max(a - b - 1, 0) for a, b in zip(A, A[1:])]))
