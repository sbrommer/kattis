instr = input()

n = len(instr)
for i in range(n):
    for j in range(i + 1, n):
        m = instr[i:j]
        instr2 = instr.replace(m, 'M')
        n = min(n, len(instr2) + len(m))

print(n)
