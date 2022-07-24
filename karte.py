line = input()

n = len(line) // 3

deck = {'P': set(), 'K': set(), 'H': set(), 'T': set()}

double = False

for i in range(n):
    suit = line[i * 3]
    number = int(line[i * 3 + 1:(i + 1) * 3])

    if number in deck[suit]:
        double = True
        break

    else:
        deck[suit].add(number)

if double:
    print('GRESKA')
else:
    for suit in 'PKHT':
        print(13 - len(deck[suit]))
