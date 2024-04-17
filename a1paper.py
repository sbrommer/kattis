input()
sheets = [int(i) for i in input().split()]

required = 2
tape = 0

for i, sheet in enumerate(sheets):
    tape += required // 2 * 2**(-(3+2*(i % 2))/4) * 0.5 ** (i // 2)
    required = (required - sheet) * 2

    if required <= 0:
        break

print('impossible' if required > 0 else tape)
