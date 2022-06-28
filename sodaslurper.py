e, f, c = map(int, input().split())

b = e + f
s = 0

while b // c:
    d, m = divmod(b, c)
    s += d
    b = d + m

print(s)
