from sys import stdin

def neighbours(i, j):
    d = [-1, 0, 1]
    return set(sum([[(i+di, j+dj) for di in d] for dj in d], []))

# Depth-first search
def dfs(dish, pixel):
    amoeba = set()
    unvisited = set([pixel])

    while unvisited:
        pixel = list(unvisited)[0]

        amoeba.add(pixel)
        unvisited.remove(pixel)

        unvisited |= set(filter(lambda n : n in dish and not n in amoeba,\
                                neighbours(*pixel)))

    return amoeba


# Read dish
m, n = list(map(int, stdin.readline().split()))

dish = set()
for i in range(m):
    line = stdin.readline()
    for j in range(n):
        if line[j] == '#':
            dish.add((i, j))

# Count amoebas
a = 0
while dish:
    a += 1
    pixel = list(dish)[0]
    amoeba = dfs(dish, pixel)

    dish = dish.difference(amoeba)
print(a)
