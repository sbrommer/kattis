from sys import stdin
from itertools import product

def readline():
    return stdin.readline().strip()

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

for word in compound:
    print(word)