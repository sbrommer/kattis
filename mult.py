n = int(input())
i = 0

while i < n - 2:
    divisor = int(input())
    dividend = int(input())
    i += 2

    while i < n and dividend % divisor:
        dividend = int(input())
        i += 1

    if i < n:
        print(dividend)
