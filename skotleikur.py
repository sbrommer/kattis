K, a, b = [int(input()) for _ in range(3)]

combinations = set()

for kills in range(K // a + 1):
    assists, mod = divmod(K - kills * a, b)

    if not mod:
        combinations |= {(kills, assists)}

print(len(combinations))
for c in combinations:
    print(*c)
