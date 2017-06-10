import sys
for line in sys.stdin.readlines():
        p = line.split("==")[0]
        if p:
                print p
