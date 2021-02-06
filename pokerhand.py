from sys import stdin

hand = stdin.readline().split()

ranks = list(map(lambda card : card[0], hand))

counts = [ranks.count(rank) for rank in set(ranks)]

print(max(counts))
