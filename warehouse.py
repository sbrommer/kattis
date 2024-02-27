from collections import defaultdict

T = int(input())

for _ in range(T):
    toys = defaultdict(int)

    N = int(input())

    for _ in range(N):
        name, nr = input().split()
        toys[name] += int(nr)

    print(len(toys))
    
    for name, nr in sorted(toys.items(), key=lambda kv: (-kv[1], kv[0])):
        print(name, nr)
