x, y, n = map(int, input().split())

for i in range(1, n+1):
    s = ''

    if not i % x:
        s += 'Fizz'
    if not i % y:
        s += 'Buzz'

    print(s if s else i)
