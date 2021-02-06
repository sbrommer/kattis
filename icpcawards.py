from sys import stdin

stdin.readline()

universities = set()

while len(universities) < 12:
    (univ, team) = stdin.readline().split()
    if univ not in universities:
        universities.add(univ)
        print(univ, team)
