t = 29260
g = 29370

w, s = map(int, input().split())
c = s * (s + 1) // 2

print((w - (t * c)) // (g - t))
