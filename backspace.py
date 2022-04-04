from sys import stdin

line = stdin.readline().strip()

stack = []

for c in line:
    if c == '<':
        stack.pop()
    else:
        stack.append(c)

print(''.join(stack))