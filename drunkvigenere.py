def to_num(c):
    return ord(c) - ord('A')


def to_char(n):
    return chr(ord('A') + n)


C = list(input().strip())
K = input().strip()

for i in range(len(C)):
    s = (i % 2) * 2 - 1
    C[i] = to_char((to_num(C[i]) + s * to_num(K[i])) % 26)

print(''.join(C))
