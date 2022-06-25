n, w, h = map(int, input().split())

for _ in range(n):
    m = int(input())

    print('DA' if m ** 2 <= w ** 2 + h ** 2 else 'NE')
