e, f, c = map(int, input().split())

b = e + f
s = 0

d, m = divmod(b, c)

while d:
    s += d
    b = d + m
    d, m = divmod(b, c)

print(s)
