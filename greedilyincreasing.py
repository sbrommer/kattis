input()

A = [int(a) for a in input().split()]
GIS = [A[0]]

for a in A[1:]:
    if a > GIS[-1]:
        GIS += [a]

print(len(GIS))
print(*GIS)
