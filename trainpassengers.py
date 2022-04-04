from sys import stdin

def readints():
    return list(map(int, stdin.readline().split()))

c, n = readints()

possible = True
left = 0
entered = 0
stayed = 0
passengers = 0
for i in range(n):
    left, entered, stayed = readints()

    passengers -= left
    if passengers < 0:
        possible = False
        break

    passengers += entered
    if passengers > c:
        possible = False
        break

    if stayed > 0 and passengers < c:
        possible = False
        break

if passengers > 0 or entered > 0 or stayed > 0:
    possible = False

print('possible' if possible else 'impossible')