alphabet = 'abcdefghijklmnopqrstuvwxyz'


def readline():
    return list(map(alphabet.index, input().strip()))


n, m = map(int, input().split())

plain = readline()
cipher = readline()

for i in range(m - 1, n - 1, -1):
    plain.insert(0, (cipher[i] - plain[n-1]) % 26)

print(*map(alphabet.__getitem__, plain), sep='')
