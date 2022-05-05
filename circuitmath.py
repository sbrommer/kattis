ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

n = int(input())
values = dict((k, v == 'T') for k, v in zip(ALPHABET, input().split()))

stack = []

for c in input().split():
    if c == '-':
        stack.append(not stack.pop())

    elif c == '*':
        left = stack.pop()
        right = stack.pop()
        stack.append(left and right)

    elif c == '+':
        left = stack.pop()
        right = stack.pop()
        stack.append(left or right)

    else:  # c is a terminal
        stack.append(values[c])

print('T' if stack[0] else 'F')
