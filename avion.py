blimps = open(0).readlines()
fbis = [i + 1 for i, b in enumerate(blimps) if 'FBI' in b]

print(*fbis if fbis else ['HE GOT AWAY!'])
