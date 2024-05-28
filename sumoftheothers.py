lines = open(0).readlines()

for line in lines:
    print(sum(map(int, line.split())) // 2)
