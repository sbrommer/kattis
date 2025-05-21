l, h = 1, 1000

while True:
    m = (l + h) // 2
    print(m)

    match input():
        case 'lower':
            h = m - 1
        case 'higher':
            l = m + 1
        case 'correct':
            break
