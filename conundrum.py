from operator import ne

line = input()
per = len(line) // 3 * 'PER'

print(sum(map(ne, line, per)))
