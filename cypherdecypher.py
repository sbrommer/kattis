from operator import mul

multiplier = list(map(int, input()))
n = int(input())

for _ in range(n):
    message = input()

    mkia = [ord(c) - ord('A')
            for c in message]

    result = [chr(mul(*m) % 26 + ord('A'))
              for m in zip(mkia, multiplier)]
              
    print(''.join(result))
