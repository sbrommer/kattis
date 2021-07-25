from sys import stdin

line = stdin.readline().strip()

scores = {'A' : 0, 'B' : 0}

for i in range(0, len(line), 2):
    scores[line[i]] += int(line[i+1])

print(max(scores, key=scores.get))
