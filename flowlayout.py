import sys

m = int(sys.stdin.readline())

while m != 0:
    (x, y)   = (0, 0)
    (w_, h_) = (0, 0)

    line = sys.stdin.readline()
    (w, h) = list(map(int, line.split()))

    while (w, h) != (-1, -1):
        if x + w <= m:
            x += w
        else:
            x = w
            y = h_
            
        w_ = max(w_, x)
        h_ = max(h_, y + h)

        line = sys.stdin.readline()
        (w, h) = list(map(int, line.split()))

    print(w_, 'x', h_)

    m = int(sys.stdin.readline())