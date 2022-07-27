n = int(input())
ts = list(map(int, input().split()))
ts.sort(reverse=True)

ts = [ts[i] + i + 1 for i in range(n)]

print(max(ts) + 1)
