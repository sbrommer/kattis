n = int(input())

for _ in range(n):
    line = input()
    print('skipped' if line == 'P=NP' else eval(line))
