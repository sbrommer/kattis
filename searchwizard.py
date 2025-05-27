from re import findall

W = input()
input()
S = input()

print(len(findall(f'(?={W})', S)))
