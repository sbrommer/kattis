from collections import defaultdict

n = int(input())

combinations = defaultdict(lambda: 0)

for _ in range(n):
    courses = list(input().split())
    courses.sort()
    courses = ''.join(courses)

    combinations[courses] += 1

counts = combinations.values()
n_attendance = max(counts)
n_popular = sum(c == n_attendance for c in counts)

print(n_popular * n_attendance)
