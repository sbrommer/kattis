from math import radians, cos, sin

g = 9.81

n = int(input())

for _ in range(n):
    v0, theta, x1, h1, h2 = list(map(float, input().split()))
    theta = radians(theta)

    t = x1 / (v0 * cos(theta))
    y = v0 * t * sin(theta) - 0.5 * g * t ** 2

    print('Safe' if h1 + 1 < y < h2 - 1 else 'Not Safe')
