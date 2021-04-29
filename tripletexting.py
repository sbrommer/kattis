from sys import stdin

s = stdin.readline().strip()

n = len(s) // 3

if s[:n] == s[n:2*n] or s[:n] == s[2*n:]:
    print(s[:n])
else:
    print(s[n:2*n])
