from collections import Counter

N = int(input())

contestants = [input() for _ in range(2*N)]
locations = contestants[1::2]
counter = Counter(locations)

print(*[f'{city} {count}' for city, count in counter.items()], sep='\n')
