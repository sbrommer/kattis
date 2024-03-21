def to_str(n, r, c):
    if r in [-n, n] and not c:
        return 'x'
    if c in [-n, n] and not r:
        return 'x'
    if r + c in [-n, n]:
        return '/'
    if abs(r) + abs(c) == n:
        return '\\'
    return ' '


n = int(input()) + 1

for r in range(-n, n + 1):
    print(''.join(to_str(n, r, c) for c in range(-n, n + 1)).rstrip())
