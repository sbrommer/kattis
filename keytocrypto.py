from sys import stdin

def unshift(i):
    return chr(ord('A') + i)

m = stdin.readline().strip()
k = stdin.readline().strip()
c = ''

for i in range(len(m)):
    c += chr(ord('A') + (ord(m[i]) - ord((k+c)[i])) % 26)

print(c)
