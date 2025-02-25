N = int(input())

wd = []
changes = set()

for _ in range(N):
    cmd = input().split()
    arg = cmd[-1]
    match cmd[0], cmd[1]:
        case 'cd', '..':
            wd = wd[:-1]

        case 'cd', _:
            wd += [arg]

        case 'nano', _:
            changes |= {'/'.join(wd+[arg])}

for path in sorted(changes):
    print(f'git add {path}')

print('git commit')
print('git push')
