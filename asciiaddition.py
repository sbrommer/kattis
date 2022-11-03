o = open(0)

line = o.readline()

n = (len(line) + 1) // 6
ascii = n * ['']

for _ in range(7):
    for i in range(n):
        ascii[i] += line[6*i:6*(i+1)-1]
    line = o.readline()

a2c = { 'xxxxxx...xx...xx...xx...xx...xxxxxx' : '0',
        '....x....x....x....x....x....x....x' : '1',
        'xxxxx....x....xxxxxxx....x....xxxxx' : '2',
        'xxxxx....x....xxxxxx....x....xxxxxx' : '3',
        'x...xx...xx...xxxxxx....x....x....x' : '4',
        'xxxxxx....x....xxxxx....x....xxxxxx' : '5',
        'xxxxxx....x....xxxxxx...xx...xxxxxx' : '6',
        'xxxxx....x....x....x....x....x....x' : '7',
        'xxxxxx...xx...xxxxxxx...xx...xxxxxx' : '8',
        'xxxxxx...xx...xxxxxx....x....xxxxxx' : '9',
        '.......x....x..xxxxx..x....x.......' : '+'}

c2a = {v: k for k, v in a2c.items()}

chars = ''.join(map(lambda a : a2c[a], ascii))
answer = eval(chars)
ascii = list(map(lambda c : c2a[c], str(answer)))

for i in range(7):
    print('.'.join([a[5*i:5*(i+1)] for a in ascii]))

