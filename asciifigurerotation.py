nl = False

while n := int(input()):
    if nl:
        print()

    figure = [input() for _ in range(n)]
    l = max(len(row) for row in figure)
    figure = [row.ljust(l) for row in figure]
    rotated = [''.join(reversed(x)).replace('-', 'x').replace('|', '-')
                                   .replace('x', '|').rstrip()
               for x in zip(*figure)]

    print(*rotated, sep='\n')
    
    nl = True
