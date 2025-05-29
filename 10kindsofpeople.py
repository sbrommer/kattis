def readints():
    return map(int, input().split())


r, c = readints()
zones = [input() for _ in range(r)]
clusters = [[0] * c for _ in range(r)]
nr = 1

for vr in range(r):
    for vc in range(c):
        if not clusters[vr][vc]:
            q = [(vr, vc)]
            clusters[vr][vc] = nr

            while q:
                (vr, vc), *q = q

                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    ur, uc = vr+dr, vc+dc

                    if 0 <= uc < c and 0 <= ur < r and \
                       not clusters[ur][uc] and \
                       zones[ur][uc] == zones[vr][vc]:

                        q += [(ur, uc)]
                        clusters[ur][uc] = nr

            nr += 1

n, = readints()

for _ in range(n):
    r1, c1, r2, c2 = [n-1 for n in readints()]
    print('neither' if clusters[r1][c1] != clusters[r2][c2] else
          'decimal' if zones[r1][c1] == '1' else 
          'binary')
