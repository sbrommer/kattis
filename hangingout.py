from sys import stdin

(l, e) = list(map(int, stdin.readline().split()))

terrace = 0
denied = 0

for _ in range(e):
    (event, n) = stdin.readline().split()
    n = int(n)
    if event == 'enter':
        if terrace + n <= l:
            terrace += n
        else:
            denied += 1
    else:
        terrace -= n

print(denied)
