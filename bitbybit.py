while n := int(input()):
    register = [None for _ in range(32)]

    for _ in range(n):
        instr, *args = input().split()
        args = [int(a) for a in args]

        match instr:
            case 'CLEAR':
                i, = args
                register[i] = 0

            case 'SET':
                i, = args
                register[i] = 1

            case 'OR':
                i, j = args

                if register[i] or register[j]:
                    register[i] = 1

                elif register[i] == 0 and register[j] == 0:
                    register[i] = 0

                else:
                    register[i] = None

            case 'AND':
                i, j = args

                if register[i] and register[j]:
                    register[i] = 1

                elif register[i] == 0 or register[j] == 0:
                    register[i] = 0

                else:
                    register[i] = None

    print(''.join(['?' if bit is None else str(bit) for bit in register[::-1]]))
