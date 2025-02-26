def parseints():
    return [int(n) for n in input().split()]


n, s, m = parseints()
board = parseints()


def fate(i, seen=set(), h=0):
    if i < 0:
        return 'left', h

    if n <= i:
        return 'right', h

    if i in seen:
        return 'cycle', h

    if board[i] == m:
        return 'magic', h

    return fate(i + board[i], seen | {i}, h+1)


print(*fate(s-1), sep='\n')
