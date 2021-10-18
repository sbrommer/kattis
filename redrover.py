from sys import stdin

instr = stdin.readline().strip()

n = len(instr)
for i in range(len(instr)):
    for j in range(i+1, len(instr)):
        m = instr[i:j]
        instr2 = instr.replace(m, 'M')
        n = min(n, len(instr2) + len(m))

print(n)
