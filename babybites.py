input()
mumbles = input().split()

makes_sense = [m == 'mumble' or int(m) == i + 1 for i, m in enumerate(mumbles)]

print('makes sense' if all(makes_sense) else 'something is fishy')
