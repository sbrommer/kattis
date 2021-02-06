import sys

line = sys.stdin.readline()[:-1]

per = 'PER' * (int(len(line) / 3))

days = 0
for i in range(len(line)):
    if line[i] != per[i]:
        days += 1

print(days)