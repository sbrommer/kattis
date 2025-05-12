def readints():
    return map(int, input().split())


R, C, N = readints()
unoccupied = {x+y*1j for x in range(R) for y in range(C)}
weak = {x-1+(y-1)*1j for x, y in [readints() for _ in range(N)]}

days = 0

while unoccupied:
    days += 1
    unoccupied, weak = unoccupied - weak, {p+d for p in weak for d in [-1, 1, -1j, 1j]} & unoccupied

print(days)
