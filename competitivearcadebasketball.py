from collections import defaultdict

n, p, m = map(int, input().split())

[input() for _ in range(n)]

score = defaultdict(int)
winners = []
max_score = 0

for _ in range(m):
    player, points = input().split()
    score[player] += int(points)

    if score[player] > max_score:
        max_score = score[player]
        winners = []

    if score[player] == max_score:
        winners += [player]

if max_score >= p:
    for winner in winners:
        print(f'{winner} wins!')
else:
    print('No winner!')
