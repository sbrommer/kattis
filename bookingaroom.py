r, n = list(map(int, input().split()))

if n == r:
    print('too late')
else:
    booked = set()
    for i in range(n):
        booked.add(int(input()))

    rooms = set(range(1,r+1))

    print(list(rooms - booked)[0])
