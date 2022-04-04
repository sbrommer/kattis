from sys import stdin

ab = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.'

line = stdin.readline().strip()

while line != '0':
    n, s = line.split()
    n = int(n)

    s = s[::-1]
    s = ''.join(map(lambda c: ab[(ab.index(c) + n) % len(ab)], s))
    
    print(s)
    
    line = stdin.readline().strip()