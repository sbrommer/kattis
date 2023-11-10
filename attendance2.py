N = int(input())
absentees = []

for _ in range(N):
    callout = input()
    if callout != 'Present!':
        absentees.append(callout)
    else:
        absentees.pop()

if absentees:
    print(*absentees, sep='\n')
else:
    print('No Absences')
