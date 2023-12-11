def readints():
    return [*map(int, input().split())]


# Empty quilt
R, C = readints()
quilt = [''.join(['.'] * C) for _ in range(R)]

# Patches
N = int(input())
patches = [[input() for _ in range(readints()[0])] for _ in range(N)]

# Sew patches onto quilt
M = int(input())
for _ in range(M):
    q, t, p = readints()
    for i, row in enumerate(patches[p - 1]):
        r = q + i
        if r < len(quilt):
            quilt[r] = f'{quilt[r][:t]}{row}{quilt[r][t+len(row):]}'[:C]

# Print quilt
print(*quilt, sep='\n')
