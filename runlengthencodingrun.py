from sys import stdin

letter, message = stdin.readline().split()

while message:
    c = message[0]

    # decode
    if letter == 'D':
        i = 2
        s = c * int(message[1])

    # encode
    else:
        i = 0
        while i < len(message) and message[i] == c:
            i += 1
        s = c + str(i)

    print(s, end = '')
    message = message[i:]
