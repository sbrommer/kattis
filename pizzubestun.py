prices = [int(pizza.split()[1]) for pizza in open(0).readlines()[1:]]

prices = sorted(prices, reverse=True)

print(sum(prices[::2]))
