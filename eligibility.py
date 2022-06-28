n = int(input())

for _ in range(n):
    name, begin, birth, courses = input().split()

    print(name)

    if int(begin[:4]) >= 2010:
        print('eligible')

    elif int(birth[:4]) >= 1991:
        print('eligible')

    elif int(courses) > 8 * 5:
        print('ineligible')

    else:
        print('coach petitions')
