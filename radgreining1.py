def replace(string, s, section):
    for i, letter in enumerate(section):
        if string[s+i-1] not in ['?', letter]:
            return 'Villa'

        string[s+i-1] = letter

    return string


n, m = map(int, input().split())

string = ['?'] * n

for _ in range(m):
    s, section = input().split()
    string = replace(string, int(s), list(section))

print(''.join(string))
