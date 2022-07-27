ab = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.'

line = input()

while line != '0':
    n, s = line.split()
    n = int(n)

    s = s[::-1]
    s = ''.join(map(lambda c: ab[(ab.index(c) + n) % len(ab)], s))
    
    print(s)
    
    line = input()
