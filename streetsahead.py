n, q = [int(n) for n in input().split()]

streets = {input(): i for i, _ in enumerate(range(n))}

for _ in range(q):
    f, t = input().split()
    print(abs(streets[t] - streets[f]) - 1)
