moves = input()

i = 0

while i < len(moves):
    if len(set(moves[i:i+3])) == 3:
        counter = 'C'
        di = 3
    else:
        match moves[i]:
            case 'R':
                counter = 'S'
            case 'B':
                counter = 'K'
            case 'L':
                counter = 'H'
        di = 1

    print(counter, end='')
    i += di
