def check_rows(board):
    for line in board:
        if line.count('W') != line.count('B') or\
           'WWW' in line or 'BBB' in line:
            return False
    return True


def transpose(xxs):
    return map(''.join, zip(*xxs))


n = int(input())
board = [input().strip() for _ in range(n)]

print(int(check_rows(board) and check_rows(transpose(board))))
