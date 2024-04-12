def special(c):
    return ord('!') <= ord(c) <= ord('*') or ord('[') <= ord(c) <= ord(']')


while True:
    try:
        n = int(input())
        s = input()

        print(''.join('\\'*(2**int(n)-1) + c if special(c) else c for c in s))
    except EOFError:
        break
