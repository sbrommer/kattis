from sys import stdin
from statistics import mean

def readint():
    return int(stdin.readline())

def group_score(scores):
    s = 0
    for i in range(len(scores)):
        s += scores[i] * (4 / 5) ** i
    return s / 5

n = readint()

scores = []
for _ in range(n):
    scores.append(readint())

print(group_score(scores))

group_scores = []
for i in range(n):
    group_scores.append(group_score(scores[:i] + scores[i+1:]))

print(mean(group_scores))