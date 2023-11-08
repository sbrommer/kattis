from operator import mul


def get_vector():
    return list(map(int, input().split()))


T = int(input())

for X in range(T):
    input()

    v1 = sorted(get_vector())
    v2 = sorted(get_vector(), reverse=True)

    Y = sum(mul(*xy) for xy in zip(v1, v2))

    print(f'Case #{X + 1}: {Y}')
