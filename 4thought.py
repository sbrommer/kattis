from sys import stdin
from itertools import product

def readint():
    return int(stdin.readline())

def mul(a, b):
    return a * b

def div(a, b):
    return a // b

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def precedence(equation):
    return list(map(lambda f: f == mul or f == div, equation))

def solve(equation):
    f1, f2, f3 = equation

    ps = precedence(equation)
    if ps == [0, 1, 1]:
        return f1(4, f3(f2(4, 4), 4))
    if ps == [1, 0, 1] or ps == [0, 0, 1]:
        return f2(f1(4, 4), f3(4, 4))
    if ps == [0, 1, 0]:
        return f3(f1(4, f2(4, 4)), 4)
    else:
        return f3(f2(f1(4, 4), 4), 4)

functions = [mul, div, add, sub]
f_str = {mul: '*', div: '/', add: '+', sub: '-'}

d = {}

equations = product(functions, functions, functions)
for equation in equations:
    f1, f2, f3 = equation
    solution = solve(equation)
    d[solution] = '4 ' + f_str[f1] + ' 4 ' + f_str[f2] + ' 4 ' + f_str[f3] + ' 4 = ' + str(solution)

m = readint()
for _ in range(m):
    n = readint()
    if n not in d.keys():
        print('no solution')
    else:
        print(d[n])