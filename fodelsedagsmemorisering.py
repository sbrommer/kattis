from sys import stdin

n = int(stdin.readline())

friends = list()
birthdays = set()

for _ in range(n):
    friend = stdin.readline().split()
    friends.append(friend)
    birthdays.add(friend[2])

groups = [list(filter(lambda f : f[2] == b, friends)) for b in birthdays]

friends = list(map(lambda g : max(g, key=lambda f : int(f[1])), groups))

friends.sort()

print(len(friends))
for f in friends:
    print(f[0])
