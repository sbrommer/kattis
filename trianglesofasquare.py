x1, y1, x2, y2 = map(int, input().split())

endpoints = {x1+y1*1j, x2+y2*1j}
corners = {0, 2024, 2024j, 2024+2024j}

print(2 - len(endpoints & corners))
