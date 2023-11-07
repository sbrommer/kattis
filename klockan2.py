d = int(input())
m = 0

while d % 3600:
    m += 1
    d -= 55

print(f'{m // 60:02d}:{m % 60:02d}')
