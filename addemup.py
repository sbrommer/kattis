def readints():
    return map(int, input().split())


flipdict = {'0': '0', '1': '1', '2': '2', '3': '-',
            '4': '-', '5': '5', '6': '9', '7': '-',
            '8': '8', '9': '6', '0': '0'}


def flip(card):
    card = ''.join(flipdict[d] for d in str(card)[::-1])
    return -1 if '-' in card else int(card)


n, s = readints()


def game():
    cards = set()

    for card in readints():
        flipped = flip(card)
        if s - card in cards or s - flipped in cards:
            return True

        cards |= {card, flipped}

    return False


print('YES' if game() else 'NO')
