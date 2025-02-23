N = int(input())
chores = [input() for _ in range(N)]

filtered = set(chores)

print(*sorted(filtered, key=chores.index), sep='\n')
