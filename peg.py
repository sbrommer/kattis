# helper functions
def parse(line):
    line = line.strip()

    if len(line) == 3:
        line = '  ' + line + '  '

    return line


def count_line(line):
    return line.count('.oo') + line.count('oo.')


def count_peg(peg):
    return sum(map(count_line, peg))


def transpose(xxs):
    return map(''.join, zip(*xxs))


# read and parse input
peg = [parse(input()) for _ in range(7)]

# count legal moves
print(count_peg(peg) + count_peg(transpose(peg)))
