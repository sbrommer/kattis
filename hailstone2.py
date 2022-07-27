n = int(input())
l = 1

while n != 1:
    l += 1
    n = n * 3 + 1 if n % 2 else n // 2

print(l)
