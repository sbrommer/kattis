n, *servers = open(0).readlines()

servers = [[piece == 'J' for piece in s.split()] for s in servers]

print(min(map(sum, zip(*servers))))
