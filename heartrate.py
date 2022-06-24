n = int(input())

for _ in range(n):
    b, p = input().split()
    b = int(b)
    p = float(p)

    bpm = 60 * b / p
    var = 60 / p

    print(bpm - var, bpm, bpm + var)
