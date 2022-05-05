N = int(input())
costumes = [input() for _ in range(N)]

counts = {c: costumes.count(c) for c in set(costumes)}

bests = [c for c in counts if counts[c] == min(counts.values())]
bests.sort()

print(*bests, sep='\n')
