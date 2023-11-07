n = int(input())
sequence = input()

match = {'(': ')', '[': ']', '{': '}'}


def valid(sequence):
    stack = []

    for bracket in sequence:
        if bracket in '([{':
            stack.append(bracket)

        else:
            if not stack or match[stack.pop()] != bracket:
                return False

    return not stack


print('Valid' if valid(sequence) else 'Invalid')
