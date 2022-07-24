def readints():
    return map(int, input().split())


n, dm = readints()
ds = list(readints())

try:
    k = [d <= dm for d in ds].index(True)
    print(f"It hadn't snowed this early in {k} years!")
except ValueError:
    print('It had never snowed this early!')
