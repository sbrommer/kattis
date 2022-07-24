N = int(input())

keys = [' ',
        '',     'abc', 'def',
        'ghi',  'jkl', 'mno',
        'pqrs', 'tuv', 'wxyz']

for i in range(N):
    print('Case #' + str(i + 1) + ':')

    sequence = ''
    word = input()

    for c in word:
        # get key number and how many presses
        number = [c in k for k in keys].index(True)
        presses = keys[number].index(c) + 1
        number = str(number)

        # append to sequence
        if len(sequence) and number == sequence[-1]:
            sequence += ' '

        sequence += number * presses

    print(sequence)
