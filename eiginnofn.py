n = int(input())

residents = [input() for _ in range(n)]
residents = {name.split()[0]: name for name in residents}

m = int(input())

for _ in range(m):
    name = input()

    if name in residents:
        if residents[name] == name:
            print('Jebb')
        else:
            print(f'Neibb en {residents[name]} er heima')
    else:
        print('Neibb')
