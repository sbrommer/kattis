def readints():
    return [int(n) for n in input().split()]


n, d = readints()
A = readints()

i = 0
total = 0

while i or not total:
    total += A[i]
    i = (i + d) % n

print(total)
