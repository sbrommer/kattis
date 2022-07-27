n = int(input())

won = sum('CD' not in input() for _ in range(n))

print(won)
