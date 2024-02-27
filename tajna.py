from math import sqrt

message = input()

L = len(message)

R = int(sqrt(L))
while L % R:
    R -= 1

print(''.join(message[i::R] for i in range(R)))
