o = open(0)

def readint():
    return int(o.readline())

n = readint()
i = 0

while i < n - 2:
    divisor  = readint()
    dividend = readint()
    i += 2

    while i < n and dividend % divisor:
        dividend = readint()
        i += 1

    if i < n:
        print(dividend)
