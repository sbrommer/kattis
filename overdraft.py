o = open(0)

def readint():
    return int(o.readline())

n = readint()

balance = 0
min_bal = 0
for _ in range(n):
    balance += readint()
    min_bal = min(min_bal, balance)

print(-min_bal)
