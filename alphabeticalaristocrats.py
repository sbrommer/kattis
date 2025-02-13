def comparable(name):
    return name[[c.isupper() for c in name].index(True):]


n = int(input())
surnames = [input() for _ in range(n)]

print(*sorted(surnames, key=comparable), sep='\n')
