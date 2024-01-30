import sys

n = int(sys.stdin.readline())
c = list(map(int, sys.stdin.readline().split()))

o = sum(1 for x in c if x % 2 != 0)

if o % 2 != 0:
    m = min(x for x in c if x % 2 != 0)
    c.remove(m)

s = sum(c)
print(s)
