from sys import stdin

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def readline():
    return list(map(alphabet.index, stdin.readline().strip()))

n, m = list(map(int, stdin.readline().split()))

plain = readline()
cipher = readline()

for i in range(m-1, n-1, -1):
    plain.insert(0, (cipher[i] - plain[n-1]) % 26)

print(''.join(map(lambda i: alphabet[i], plain)))