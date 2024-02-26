input()

sevens = ['7' in input() for _ in range(3)]

print('777' if all(sevens) else '0')
