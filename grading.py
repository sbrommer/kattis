limits = map(int, input().split())
grade = int(input())

i = sum(map(grade.__lt__, limits))

print('ABCDEF'[i])
