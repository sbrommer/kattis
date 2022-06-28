N = int(input())

for _ in range(N):
    a, b, c = map(int, input().split())

    if a + b == c:
        print('Possible')

    elif max(a, b) - min(a, b) == c:
        print('Possible')

    elif a * b == c:
        print('Possible')

    elif max(a, b) / min(a, b) == c:
        print('Possible')

    else:
        print('Impossible')
