B = int(input())
Ds = input().split()
X = input()


n = 0

while X:
    for i, D in enumerate(Ds):
        if X.startswith(D):
            n = n * B + i
            X = X[len(D):]

print(n)
