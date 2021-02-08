from sys import stdin

n = int(stdin.readline())
ts = list(map(int, stdin.readline().split()))
ts.sort(reverse=True)

ts = [ts[i]+i+1 for i in range(n)]

print(max(ts)+1)
