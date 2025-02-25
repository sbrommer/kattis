a, b, c = sorted(map(int, input().split()))

if a*a + b*b == c*c:
    print(a*b//2)
else:
    print(-1)
