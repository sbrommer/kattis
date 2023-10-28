v = int(input())
n = int(input())

for _ in range(n):
    s, k = input().split()
    k = int(k)
    print(s, end=' ')
    print('opin' if k >= v else 'lokud')
