from sys import stdin

line = stdin.readline()[:-1]

print('yup' if line == 'OCT 31' or line == 'DEC 25' else 'nope')
