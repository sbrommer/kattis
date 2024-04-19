n = int(input())

for _ in range(n):
    s, d = map(int, input().split())

    b = (s - d) / 2

    if b < 0 or b % 1:
        print('impossible')

    else:
        b = int(b)
        a = s - b

        print(a, b)
