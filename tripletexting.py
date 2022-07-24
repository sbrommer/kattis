s = input()

n = len(s) // 3

if s[:n] in [s[n:2*n], s[2*n:]]:
    print(s[:n])
else:
    print(s[n:2*n])
