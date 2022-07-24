n = int(input())

balance = 0
min_bal = 0
for _ in range(n):
    balance += int(input())
    min_bal = min(min_bal, balance)

print(-min_bal)
