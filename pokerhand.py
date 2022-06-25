hand = input().split()

ranks = [card[0] for card in hand]

counts = [ranks.count(rank) for rank in set(ranks)]

print(max(counts))
