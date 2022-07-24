m = input()
k = input()
c = ''

for i in range(len(m)):
    c += chr(ord('A') + (ord(m[i]) - ord((k+c)[i])) % 26)

print(c)
