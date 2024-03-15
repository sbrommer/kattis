string = input()
sentence = input().split()

mapping = set(zip(string, sentence))
characters = set(m[0] for m in mapping)
words = set(m[1] for m in mapping)

print(len(string) == len(sentence) and
      len(mapping) == len(characters) == len(words))
