from sys import stdin

line = stdin.readline()

n = (len(line) + 1) // 4
ascii = n * ['']

for _ in range(5):
    for i in range(n):
        ascii[i] += line[4*i:4*i+3]
    line = stdin.readline()

digits = { '**** ** ** ****' : 0,
           '  *  *  *  *  *' : 1,
           '***  *****  ***' : 2,
           '***  ****  ****' : 3,
           '* ** ****  *  *' : 4,
           '****  ***  ****' : 5,
           '****  **** ****' : 6,
           '***  *  *  *  *' : 7,
           '**** ***** ****' : 8,
           '**** ****  ****' : 9}

if not all(map(lambda a : a in digits.keys(), ascii)):
    print('BOOM!!')
else:
    n = int(''.join(map(lambda a : str(digits[a]), ascii)))
    print('BOOM!!' if n % 6 else 'BEER!!')
