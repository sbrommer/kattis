n = int(input())
k = int(input())

if k >= n:
    print('impossible')

else:
    for bottle in range(k):
        print(f'open {bottle+2} using 1')
