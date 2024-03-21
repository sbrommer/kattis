commands = [line.split() for line in open(0).readlines()]

vars = {'<': '<', '>': '>', '=': '=='}

for type, *args in commands:
    match type:
        case 'define':
            i, x = args
            vars[x] = i

        case 'eval':
            if any(a not in vars for a in args):
                print('undefined')
            else:
                comparison = ''.join(vars[a] for a in args)
                print('true' if eval(comparison) else 'false')
