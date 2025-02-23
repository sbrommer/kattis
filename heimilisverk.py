N = int(input())
chores = [input() for _ in range(N)]

seen = set()
for chore in chores:
    if chore not in seen:
        print(chore)
        seen |= {chore}
