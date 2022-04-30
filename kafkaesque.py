o = open(0)

K = int(o.readline())
passes = 1
previous = 0

for _ in range(K):
    clerk = int(o.readline())
    passes += clerk < previous
    previous = clerk

print(passes)
