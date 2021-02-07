from sys import stdin

n = int(stdin.readline())

keys = [' ', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

for i in range(n):
    print('Case #' + str(i+1) + ':', end=' ')

    prev_key = ''
    word = stdin.readline()[:-1]

    for c in word:
        key = list(filter(lambda k : c in k, keys))[0]

        if key == prev_key:
            print(' ', end='')
        prev_key = key

        number = keys.index(key)
        presses = key.index(c) + 1

        print(str(number) * presses, end='')

    print()
