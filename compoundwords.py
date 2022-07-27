o = open(0)


def readline():
    return o.readline().strip()


words = set()

line = readline()
while line != '':
    words |= set(line.split())
    line = readline()

compound = set()

for word1 in words:
    for word2 in words:
        if word1 != word2:
            compound.add(word1 + word2)

compound = list(compound)
compound.sort()

print(*compound)
