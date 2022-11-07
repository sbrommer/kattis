input()
s = int(input(), 2)

b = format(s | s // 2 | s // 4, 'b')

print(b.count('1'))
