P = int(input())

for _ in range(P):
    K, N = map(int, input().split())
    print(K, (N ** 2 + 3 * N) // 2)
