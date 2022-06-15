o = open(0)

n = int(o.readline())
H = set()
L = set()

while n:
    response = o.readline().strip()

    if response == 'too high':
        H.add(n)

    if response == 'too low':
        L.add(n)

    if response == 'right on':
        if all(n < h for h in H) and all(l < n for l in L):
            print('Stan may be honest')
        else:
            print('Stan is dishonest')

        H = set()
        L = set()

    n = int(o.readline())
