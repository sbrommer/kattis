def readints():
    return [*map(int, input().split())]


input()
s1 = sum(readints())
s2 = sum(readints())

if s1 > s2:
    print('Button 1')
elif s1 < s2:
    print('Button 2')
else:
    print('Oh no')
