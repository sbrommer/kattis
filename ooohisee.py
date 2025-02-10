R, X = map(int, input().split())

map_ = {r+c*1j: m for r in range(1, R+1) for c, m in enumerate(input(), 1)}


def is_treasure(p):
    ds = [-1-1j, -1, -1+1j, -1j, 1j, 1-1j, 1, 1+1j]
    return map_[p] == '0' and all(map_.get(p+d) == 'O' for d in ds)


ts = [p for p in map_ if is_treasure(p)]

if not ts:
    print('Oh no!')
elif len(ts) != 1:
    print(f'Oh no! {len(ts)} locations')
else:
    print(f'{int(ts[0].real)} {int(ts[0].imag)}')
