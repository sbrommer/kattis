g, r = map(int, input().split())

health = min(r, g) * 10
g -= min(r, g)

health += (g // 3) * 10
health += [0, 1, 3][g % 3]

print(health)
