from sys import stdin

def readints():
    return list(map(int, stdin.readline().split()))

n, dm = readints()
ds = readints()

try:
    k = [d <= dm for d in ds].index(True)
    print(f"It hadn't snowed this early in {k} years!")
except ValueError:
    print('It had never snowed this early!')
