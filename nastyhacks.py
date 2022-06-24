n = int(input())

for _ in range(n):
    r, e, c = map(int, input().split())
    if r < e - c:
        print('advertise')
    if r > e - c:
        print('do not advertise')
    if r == e - c:
        print('does not matter')
