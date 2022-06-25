from re import finditer

print(*[pos.start() for pos in finditer('[:;]-?\)', input())])
