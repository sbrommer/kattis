n = int(input())

qaly = 0

for _ in range(n):
    line = input()
    q, y = [float(i) for i in line.split()]
    qaly += q * y

print(qaly)
