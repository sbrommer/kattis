import sys
from math import ceil, sin, radians

(h, v) = list(map(int, sys.stdin.readline().split()))

print(ceil(h / sin(radians(v))))