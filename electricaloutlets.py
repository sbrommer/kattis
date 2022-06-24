n = int(input())

for _ in range(n):
    k, *os = map(int, input().split())
    print(1 + sum(os) - k)
