def direction(a, b):
    ns = ['North', 'East', 'South', 'West']

    match (ns.index(b) - ns.index(a)) % 4:
        case 1:
            return 'left'
        case 2:
            return 'straight'
        case 3:
            return 'right'


def rightofway(arrive, leave, other):
    return (direction(arrive, leave) == 'straight' and
            direction(arrive, other) == 'right') or \
           (direction(arrive, leave) == 'left' and
            direction(arrive, other) in ['straight', 'right'])


print('Yes' if rightofway(*input().split()) else 'No')
