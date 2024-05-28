n, e = map(int, input().split())
e = str(2 ** e)

print(sum(e in str(i) for i in range(n + 1)))
