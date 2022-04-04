from sys import stdin

ps = list(map(int, stdin.readline().split()))

while ps != [1, 2, 3, 4, 5]:
    for i in range(4):
        if ps[i] > ps[i+1]:
            ps[i], ps[i+1] = ps[i+1], ps[i]
            for p in ps:
                print(p, end=' ')
            print()
