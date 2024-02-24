def adventure(a):
    bag = []
    for c in a:
        if c in '$|*':
            bag += c
        elif c in 'tjb' and (not bag or '|*$'['tjb'.index(c)] != bag.pop()):
            return False
    return not bag


n = int(input())

for _ in range(n):
    a = input()
    print('YES' if adventure(a) else 'NO')
