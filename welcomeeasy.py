def count_subsequences(xs, ys):
    if not ys:
        return 1

    if not xs:
        return 0

    dont_pick = count_subsequences(xs[1:], ys)

    if xs[0] == ys[0]:
        return count_subsequences(xs[1:], ys[1:]) + dont_pick

    return dont_pick


welcome = 'welcome to code jam'

T = int(input())

for i in range(T):
    line = [c for c in input() if c in welcome]
    n = count_subsequences(line, welcome)

    print(f'Case #{i + 1}: {n:04d}')
