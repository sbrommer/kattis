inp = open(0).read()

logs = [log.split('\n') for log in inp.strip().split('\n\n')]

for log in logs:
    l = len(log[0])
    t = 0

    for line in log:
        n = line.count('*')
        print('.' * (l - n - t) + '*' * n + '.' * t)
        t += n

    print()
