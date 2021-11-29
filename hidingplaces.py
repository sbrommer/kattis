from sys import stdin

def str2loc(s):
    x = ord(s[0]) - ord('a')
    y = int(s[1]) - 1
    return x, y

def loc2str(loc):
    return chr(ord('a') + loc[0]) + str(loc[1] + 1)

def valid(x, y):
    return 0 <= x <= 7 and 0 <= y <= 7

def reachable(loc):
    x, y = loc
    dx = [-2, -2, -1, -1,  1, 1,  2, 2]
    dy = [-1,  1, -2,  2, -2, 2, -1, 1]

    locs = set()
    for i in range(8):
        loc2 = (x + dx[i], y + dy[i])
        if valid(*loc2):
            locs.add(loc2)
    return locs

def bfs(locs, d = 0, visited = set()):
    reachables = set().union(*map(reachable, locs))
    unvisited  = reachables.difference(visited)
    visited    = visited.union(unvisited)

    if not len(unvisited):
        return d, locs

    return bfs(unvisited, d + 1, visited)

n = int(stdin.readline())

for _ in range(n):
    loc = str2loc(stdin.readline().strip())
    d, locs = bfs(set([loc]))

    locs = list(locs)
    locs.sort(key = lambda loc : loc[0])
    locs.sort(key = lambda loc : loc[1], reverse = True)

    print(d, *map(loc2str, locs))
