import sys
inp = sys.stdin.readline
n = int(inp())

c = 1000 - n

cur = [500, 100, 50, 10, 5, 1]
cnt = 0

for i in cur:
    cnt += c // i
    c %= i

print(cnt)
