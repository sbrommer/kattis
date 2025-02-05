def readint():
    return int(input())


a = readint()
b = readint()

print('MAGA!'      if a > b else
      'FAKE NEWS!' if b > a else
      'WORLD WAR 3!')
