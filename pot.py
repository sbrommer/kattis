n = int(input())

print(sum(pow(*divmod(int(input()), 10)) for _ in range(n)))
