N = int(input())

o = '+' + '-' * N + '+'
m = '|' + ' ' * N + '|'

print(*([o] + [m] * N + [o]), sep='\n')
