gifts = [line.split() for line in open(0).readlines()[1:]]

print(max(gifts, key=lambda gift: int(gift[1]))[0])
