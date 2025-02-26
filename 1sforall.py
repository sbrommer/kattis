from math import log10

n = int(input())

mem = [10**5] * (n+1)
mem[1] = 1

for i in range(2, n+1):
    # add
    for x in range(1, i // 2 + 1):
        mem[i] = min(mem[i], mem[x] + mem[i - x])

    # multiply
    for x in range(2, int(i ** 0.5) + 1):
        if not i % x:
            mem[i] = min(mem[i], mem[x] + mem[i // x])

    # concat
    for x in range(1, int(log10(i))+1):
        d, m = divmod(i, 10**x)
        if m >= 10**(x-1):
            mem[i] = min(mem[i], mem[d] + mem[m])

print(mem[n])
