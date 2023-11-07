n = int(input())
friends = input().split()

mantra = 'Úllen dúllen doff kikke lane koff koffe lane bikke bane úllen dúllen doff.'
m = len(mantra.split())

f = m % n
print(friends[f - 1])
