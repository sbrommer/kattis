h, m = map(int, input().split())

dh = m < 45

h = (h - dh) % 24
m = (m - 45) % 60

print(h, m)
