import sys

problems = sys.stdin.readline()[:-1].split(';')
problems = map(lambda problem : problem.split('-'), problems)

n = 0

for problem in problems:
    if len(problem) > 1:
        (l, h) = list(map(int, problem))
        n += h - l
    n += 1
    
print(n)