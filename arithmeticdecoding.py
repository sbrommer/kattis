N = int(input())
D = int(input())
binary = input()

k = sum(int(bit) * 2 ** -i for i, bit in enumerate(binary[2:], 1))
pA = D / 8
a, b = 0, 1

for _ in range(N):
    c = a + pA * (b - a)
    if a <= k < c:
        print('A', end='')
        a, b = a, c
    else:
        print('B', end='')
        a, b = c, b
print()
