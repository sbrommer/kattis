A, B = map(int, input().split())
N = int(input())
floors = [int(input()) for _ in range(N)]

print(abs(B - A) * 4 + sum(A < a < B or B < a < A for a in floors) * 10)
