from sys import stdin

def solve(a, b, c):
    if a == b + c:
        return '=', '+'
    if a == b - c:
        return '=', '-'
    if a == b / c:
        return '=', '/'
    if a == b * c:
        return '=', '*'
    if a + b == c:
        return '+', '='
    if a - b == c:
        return '-', '='
    if a / b == c:
        return '/', '='
    if a * b == c:
        return '*', '='

a, b, c = list(map(int, stdin.readline().split()))

o1, o2 = solve(a, b, c)

print(str(a)+str(o1)+str(b)+str(o2)+str(c))
