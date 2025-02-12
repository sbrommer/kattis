d = dict()
N = int(input())

for _ in range(N):

    obj, *args = input().split()

    match obj:
        case 'OG':
            a, b, n = args
            d[n] = d[a] and d[b]
        case 'EDA':
            a, b, n = args
            d[n] = d[a] or d[b]
        case 'EKKI':
            a, n = args
            d[n] = not d[a]
        case 'INNTAK':
            n, v = args
            d[n] = v == 'SATT'
        case 'UTTAK':
            n, = args
            print(f'{n} {"SATT" if d[n] else "OSATT"}')
