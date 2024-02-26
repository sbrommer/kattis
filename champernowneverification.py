def k(n, i=1):
    if not n:
        return i - 1

    s = str(i)
    if n.startswith(s):
        return k(n[len(s):], i + 1)

    return -1


print(k(input()))
