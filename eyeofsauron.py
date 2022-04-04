drawing = open(0).readline().strip()

left, right = map(len, drawing.split('()'))

print('correct' if left == right else 'fix')
