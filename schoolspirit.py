from statistics import mean


def group_score(scores):
    return sum(s * (4 / 5) ** i for i, s in enumerate(scores)) / 5


n = int(input())

scores = [int(input()) for _ in range(n)]

print(group_score(scores))

group_scores = [group_score(scores[:i] + scores[i+1:]) for i in range(n)]

print(mean(group_scores))
