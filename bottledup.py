s, v1, v2 = map(int, input().split())

n1 = s // v1

while n1 >= 0 and n1*v1 + ((s - n1 * v1) // v2)*v2 != s:
    n1 -= 1

if n1 >= 0:
    print(n1, (s - n1 * v1) // v2)
else:
    print('impossible')
