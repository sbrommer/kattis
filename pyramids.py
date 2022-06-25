from math import ceil

N = int(input())

l = ceil((3 * N / 4) ** (1 / 3))
b = l * (4 * l ** 2 - 1) // 3

print(l - (b > N))
