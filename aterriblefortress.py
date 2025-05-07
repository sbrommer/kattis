from re import findall

print(sum(map(int, findall(r'\d+', open(0).read())[1:])))
