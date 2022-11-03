from collections import defaultdict

def get_report():
    report = defaultdict(lambda: set())

    for _ in range(n):
        name, *items = input().split()

        for item in items:
            report[item].add(name)

    return report


def print_report(report):
    items = list(report.keys())
    items.sort()
    for item in items:
        print(item, end=' ')

        names = list(report[item])
        names.sort()
        print(*names, sep=' ')
    print()

n = int(input())

while n:
    report = get_report()
    print_report(report)

    n = int(input())
