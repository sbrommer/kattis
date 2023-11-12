m, n, *lanes = open(0).readlines()

cells = int(m) * int(n)
empty = sum(lane.count('.') for lane in lanes)

print(empty / cells)
