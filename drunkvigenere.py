from sys import stdin

def to_num(c):
    return ord(c) - ord('A')

def to_char(n):
    return chr(ord('A') + n)

C = list(stdin.readline().strip())
K = stdin.readline().strip()

for i in range(len(C)):
    s = -1 if i % 2 == 0 else 1
    C[i] = to_char((to_num(C[i]) + s * to_num(K[i])) % 26)

print(''.join(C))
