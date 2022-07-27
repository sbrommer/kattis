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


a, b, c = map(int, input().split())

o1, o2 = solve(a, b, c)

print(str(a) + str(o1) + str(b) + str(o2) + str(c))
