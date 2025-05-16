n = int(input())
cards = [int(c) % 2 for c in input().split()]
stack = []

for card in cards:
    if stack and stack[-1] == card:
        stack = stack[:-1]
    else:
        stack += [card]

print(len(stack))
