from sys import stdin

r, n = list(map(int, stdin.readline().split()))

if n == r:
    print('too late')
else:
    booked = set()
    for i in range(n):
        booked.add(int(stdin.readline()))

    rooms = set(range(1,r+1))

    print(list(rooms - booked)[0])