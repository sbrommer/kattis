from operator import add, mul

A = int(input())
o = {'+': add, '*': mul}[input().strip()]
B = int(input())

print(o(A, B))
