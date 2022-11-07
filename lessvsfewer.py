table1 = dict([('number', 'c'), ('amount', 'm'), ('most', 'cm'),
               ('fewest', 'c'), ('least', 'm'), ('more', 'cm'), ('fewer', 'c'),
               ('less', 'm'), ('many', 'c'), ('much', 'm'), ('few', 'c'),
               ('little', 'm')])

n, p = [int(i) for i in input().split()]

nouns = dict(input().split() for _ in range(n))
    
for _ in range(p):
    line = input().split()
    phrase, noun = line[0], line[-1]
    print('Correct!' if nouns[noun] in table1[phrase] else 'Not on my watch!')
