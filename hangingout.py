l, e = map(int, input().split())

terrace = 0
denied = 0

for _ in range(e):
    event, n = input().split()
    n = int(n)

    if event == 'enter':
        if terrace + n <= l:
            terrace += n
        else:
            denied += 1
    else:
        terrace -= n

print(denied)
