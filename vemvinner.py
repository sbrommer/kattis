game = [tuple(input().split()) for _ in range(3)]

lines = game + list(zip(*game)) + \
        [(game[0][0], game[1][1], game[2][2]),
         (game[0][2], game[1][1], game[2][0])]

if ('X', 'X', 'X') in lines:
    print('Johan har vunnit')
elif ('O', 'O', 'O') in lines:
    print('Abdullah har vunnit')
else:
    print('ingen har vunnit')
