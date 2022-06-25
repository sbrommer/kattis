from math import factorial

T = int(input())

for _ in range(T):
    print(factorial(int(input())) % 10)
