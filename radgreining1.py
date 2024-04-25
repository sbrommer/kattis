def solve():
    n, m = map(int, input().split())

    string = ['?'] * n

    for _ in range(m):
        s, section = input().split()
        s, section = int(s), list(section)

        for i, letter in enumerate(section, -1):
            if string[s+i] not in ['?', letter]:
                return 'Villa'

            string[s+i] = letter

    return ''.join(string)


print(solve())
