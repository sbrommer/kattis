N = int(input())

words = [input().lower() for _ in range(N)]
sentence = input().lower()

print('Hi, how do I look today?'
      if all(word in words for word in sentence.split()) else
      'Thore has left the chat')
