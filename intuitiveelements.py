t = int(input())

for _ in range(t):
    element = input()
    abbreviation = input()
    print('YES' if all(c in element for c in abbreviation) else 'NO')
