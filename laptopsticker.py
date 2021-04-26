from sys import stdin

[wc,hc,ws,hs] = list(map(int, stdin.readline().split()))

print(1 if wc > ws+1 and hc > hs+1 else 0)
