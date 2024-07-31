friend = input()
N = int(input())

for i in range(N):
    name = input()
    if len(friend) == len(name) and \
       sum(f != n for f, n in zip(friend, name)) <= 1:
        print(i + 1)
        break
