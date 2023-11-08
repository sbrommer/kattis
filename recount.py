from collections import Counter

votes = open(0).readlines()[:-1]

counter = Counter(votes)
max_count = max(counter.values())
winners = [name for name, count in counter.items() if count == max_count]

print(winners[0] if len(winners) == 1 else 'Runoff!')
