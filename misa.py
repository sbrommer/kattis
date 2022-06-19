o = open(0)

R, S = [int(n) for n in o.readline().split()]
seating = [o.readline().strip() for _ in range(R)]


def neighbours(r, s):
    return [(r + y, s + x)
            for x in [-1, 0, 1]
            for y in [-1, 0, 1]
            if (x, y) != (0, 0)
            and 0 <= r + y < R
            and 0 <= s + x < S]


shakes = [[sum(seating[rn][sn] == 'o'
           for rn, sn in neighbours(r, s))
           for s in range(S)]
           for r in range(R)]

os   = [(r, s) for r in range(R) for s in range(S) if seating[r][s] == 'o']
dots = [(r, s) for r in range(R) for s in range(S) if seating[r][s] == '.']

best = max(shakes[r][s] for r, s in dots) if dots else 0
print(sum(shakes[r][s] for r, s in os) // 2 + best)
