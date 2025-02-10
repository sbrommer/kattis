n, a, b = map(int, input().split())
r = range(1, n+1)

f = sum(not(i % a) for i in r)
b = sum(not(i % b) for i in r)
fb = sum(not(i % a) and not(i % b) for i in r)

print(f-fb, b-fb, fb)
