n = int(input())

teeth = [{'+': set(range(1, 9)), '-': set(range(1, 9))},
         {'+': set(range(1, 9)), '-': set(range(1, 9))}]

can_eat = [True, True]

for _ in range(n):
    tooth, problem = input().split()

    # parse tooth
    side = tooth[1] in '+-'
    jaw = tooth[side]
    number = int(tooth[not side])

    # pull tooth
    teeth[side][jaw].remove(number)

    # update whether Bluetooth can eat
    can_eat[side] = can_eat[side] and problem != 'b' and\
        bool(teeth[side]['+']) and bool(teeth[side]['-'])

print(2 if not any(can_eat) else int(can_eat[1]))
