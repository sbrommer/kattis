from sys import stdin

n = int(stdin.readline())

inside = set()
for _ in range(n):
    action, employee = stdin.readline().split()

    if action == 'entry':
        if employee in inside:
            print(employee, 'entered (ANOMALY)')
        else:
            print(employee, 'entered')
            inside.add(employee)
            
    if action == 'exit':
        if employee not in inside:
            print(employee, 'exited (ANOMALY)')
        else:
            print(employee, 'exited')
            inside.remove(employee)