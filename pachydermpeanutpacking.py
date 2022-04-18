# Parse functions
o = open(0)


def readint():
    return int(o.readline())


def readline():
    line = o.readline().split()
    return list(map(float, line[:-1])), line[-1]


# Solution
n = readint()

while n:
    # Get boxes
    boxes = [readline() for _ in range(n)]

    # Inspect each peanut
    m = readint()
    for _ in range(m):
        # Get peanut
        [x, y], peanut_type = readline()

        # Initialise
        print(peanut_type, end=' ')
        floor = True

        # Check every box
        for [x1, y1, x2, y2], box_type in boxes:

            if x1 <= x <= x2 and y1 <= y <= y2:
                if peanut_type == box_type:
                    print('correct')
                else:
                    print(box_type)

                floor = False

        # If no box matches
        if floor:
            print('floor')

    n = readint()

    print()
