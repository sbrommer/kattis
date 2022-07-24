s = input()

z = len(s)

print(z)

x = 0
y = 0

for q in s:
    x *= 2
    y *= 2
    
    q = int(q)

    x += q % 2
    y += q == 2 or q == 3

print(x, y)
