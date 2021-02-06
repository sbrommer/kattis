import sys

dominant = {'A' : 11, 'K' : 4, 'Q' : 3, 'J' : 20, 'T' : 10, '9' : 14 , '8' : 0, '7' : 0}
not_dominant = {'A' : 11, 'K' : 4, 'Q' : 3, 'J' : 2, 'T' : 10, '9' : 0 , '8' : 0, '7' : 0}

line = sys.stdin.readline()
(n, b) = line.split()
n = int(n)

points = 0

for _ in range(n*4):
    card = sys.stdin.readline()

    if card[1] == b:
        points += dominant[card[0]]
    else:
        points += not_dominant[card[0]]

print(points)