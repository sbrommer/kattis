input()

universities = set()

while len(universities) < 12:
    univ, team = input().split()

    if univ not in universities:
        universities.add(univ)
        print(univ, team)
