from sys import stdin

n = int(stdin.readline())

for _ in range(n):
    name, begin, birth, courses = stdin.readline().split()

    print(name, end=' ')

    if int(begin[:4]) >= 2010:
        print('eligible')

    elif int(birth[:4]) >= 1991:
        print('eligible')

    elif int(courses) > 8 * 5:
        print('ineligible')

    else:
        print('coach petitions')
