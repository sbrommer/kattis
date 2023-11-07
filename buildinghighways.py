N = int(input())
As = list(map(int, input().split()))

# Connect every city to the city with the
# lowest difficulty level. This costs
# Ai + min(As) for city i. So for all cities,
# the cost is sum(As) + N * min(As). Subtract the
# costs of the city with the lowest difficulty level
# to itself, which is 2 * min(As). This gives
# sum(As) + N * min(As) - 2 * min(As), which equals:

print(sum(As) + (N - 2) * min(As))
