def readint():
    return int(input())


n = readint()

recited = set(readint() for _ in range(n))
good_job = set(range(1, max(recited)))

if not good_job - recited:
    print('good job')

else:
    missing = list(good_job - recited)
    missing.sort()
    print(*missing)
