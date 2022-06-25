ps = [sum(map(int, line.split())) for line in open(0).readlines()]

print(*[(i+1, x) for i, x in enumerate(ps) if x == max(ps)][0])
