line = open(0).readline().strip()

ix = [i for i, c in enumerate(line) if c.isupper()]

nops = 0

for i in ix:
    m = (i + nops) % 4
    if m:
        nops += 4 - m

print(nops)
