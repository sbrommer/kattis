# Surfaces of pieces.
pieces = {1: [[0], [0, 0, 0, 0]],
          2: [[0, 0]],
          3: [[0, 0, 1], [1, 0]],
          4: [[1, 0, 0], [0, 1]],
          5: [[0, 0, 0], [0, 1], [1, 0, 1], [1, 0]],
          6: [[0, 0, 0], [0, 0], [0, 1, 1], [2, 0]],
          7: [[0, 0, 0], [0, 2], [1, 1, 0], [0, 0]]}


# Get surfaces of playing field.
def surfaces(l):
    ss = []
    for i in [1, 2, 3, 4]:
        for j in range(len(l) - i + 1):
            s = l[j: j + i]
            s = list(map(lambda x: x - min(s), s))
            ss.append(s)
    return ss


# Read and parse data.
cp, hs = open(0).readlines()

c, p = map(int, cp.split())
hs = list(map(int, hs.split()))

# Solution.
print(sum(s1 == s2 for s1 in pieces[p] for s2 in surfaces(hs)))
