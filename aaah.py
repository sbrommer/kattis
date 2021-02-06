import sys

able_to_say = sys.stdin.readline()
wants_to_hear = sys.stdin.readline()

if len(able_to_say) >= len(wants_to_hear):
    print("go")
else:
    print("no")
