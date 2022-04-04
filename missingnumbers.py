from sys import stdin

def readint():
    return int(stdin.readline())

n = readint()

recited = set()
for i in range(n):
    recited.add(readint())


good_job = set(range(1, max(recited)))
if not good_job - recited:
    print('good job')
else:
    missing = list(good_job - recited)
    missing.sort()
    for m in missing:
        print(m)
