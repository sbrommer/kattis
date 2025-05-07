i = int(input())
w = int(input())
l = w if i == 1 else int(input())
h = 3 if i <= 2 else int(input())

print((w*h*2 + l*h*2 + w*l) - (h*4 + w*2 + l*2) + 4)
