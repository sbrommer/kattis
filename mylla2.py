def transpose(game):
    return [''.join(line) for line in zip(*game)]


def win_row(game):
    return any(row == 'OOO' for row in game)


def win_col(game):
    return win_row(transpose(game))


def win_diag(game):
    return [game[0][0], game[1][1], game[2][2]] == ['O', 'O', 'O'] or \
           [game[0][2], game[1][1], game[2][0]] == ['O', 'O', 'O']


game = [line.strip() for line in open(0).readlines()]

print('Jebb'
      if win_row(game) or win_col(game) or win_diag(game)
      else 'Neibb')
