def error(code):
    match = {'(': ')', '[': ']', '{': '}'}

    stack = []

    for i, c in enumerate(code):
        if c in '([{':
            stack.append(c)
        elif c in ')]}':
            if not stack or match[stack.pop()] != c:
                return f'{c} {i}'

    return 'ok so far'


input()

print(error(input()))
