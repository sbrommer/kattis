from sys import stdin

d = {}

line = stdin.readline()
while line != '\n':
    english, foreign = line.split()
    d[foreign] = english
    line = stdin.readline()

foreign = stdin.readline().strip()
while foreign != '':
    if foreign not in d.keys():
        print('eh')
    else:
        print(d[foreign]) 
    foreign = stdin.readline().strip()