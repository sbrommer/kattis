from sys import stdin

def get_report():
    report = dict()

    for _ in range(n):
        name, *items = stdin.readline().split()

        for item in items:
            if item not in report.keys():
                report[item] = set()

            report[item].add(name)

    return report


def print_report(report):
    items = list(report.keys())
    items.sort()
    for item in items:
        print(item, end=' ')

        names = list(report[item])
        names.sort()
        for name in names:
            print(name, end=' ')
        print()
    print()

n = int(stdin.readline())

while n:
    report = get_report()
    print_report(report)

    n = int(stdin.readline())
