r, c = [int(n) for n in input().split()]

print((r * (r - 1) ** (c - 1)) % 998_244_353)
