n = int(input())

alphabet = set('abcdefghijklmnopqrstuvwxyz')

for _ in range(n):
    phrase = set(map(str.lower, input()))
    missing = alphabet - phrase

    missing = ''.join(sorted(list(missing)))

    if not missing:
        print('pangram')
    else:
        print('missing', missing)
