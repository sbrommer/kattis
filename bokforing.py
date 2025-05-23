from collections import defaultdict

N, Q = map(int, input().split())
wealth = defaultdict(int)

for _ in range(Q):
    event, *args = input().split()

    match event:
        case 'SET':
            i, x = args
            wealth[i] = x

        case 'RESTART':
            x, = args
            wealth = defaultdict(lambda x=x: x)

        case 'PRINT':
            i, = args
            print(wealth[i])
