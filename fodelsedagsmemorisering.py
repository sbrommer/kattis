from itertools import groupby


def parsefriend(line):
    name, like, birthday = line.split()
    day, month = birthday.split('/')
    return (int(month), int(day), -int(like), name)


friends = sorted(map(parsefriend, open(0).readlines()[1:]))

remember = [next(g)[3] for _, g in groupby(friends, key=lambda f: f[:2])]

print(len(remember), *sorted(remember))
