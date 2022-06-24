from statistics import mean

input()
print(mean(filter(lambda b: b >= 0, map(int, input().split()))))
