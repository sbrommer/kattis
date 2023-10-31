n = int(input())

m = 0
uvcs = ''

for i in range(n):
    cs = input().split()
    for j in range(n):
        if int(cs[j]) > 0:
            m += 1
            uvcs += f'{i + 1} {j + 1} {cs[j]}\n'

print(m)
print(uvcs)
