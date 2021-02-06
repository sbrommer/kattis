import sys

(p1, p2) = sys.stdin.readline().split()
n = int(sys.stdin.readline())

def valid_match(match):
    if len(match) < 2 or len(match) > 3:
        return False

    if not valid_set(match[0]) or not valid_set(match[1]):
        return False

    if len(match) == 2 and winner(match[0]) != winner(match[1]):
        return False

    if len(match) == 3:
        if winner(match[0]) == winner(match[1]):
            return False

        if not valid_last_set(match[2]):
            return False

    if p1 == 'federer':
        return winner(match[0]) == 0 and winner(match[1]) == 0
    if p2 == 'federer':
        return winner(match[0]) == 1 and winner(match[1]) == 1

    return True

def winner(set):
    return set[0] < set[1]

def valid_set(set):
    winner = int(max(set))
    loser = int(min(set))

    if winner < 6 or winner > 7:
        return False

    if loser == 6:
        return winner == 7

    return winner - loser >= 2

def valid_last_set(set):
    set = list(map(int,set))
    winner = max(set)
    loser = min(set)


    if loser >= 6:
        return winner - loser == 2

    return valid_set(set)

for _ in range(n):
    match = sys.stdin.readline().split()
    match = list(map(lambda s : s.split(':'), match))
    
    print('da' if valid_match(match) else 'ne')