import sys
input = sys.stdin.readline

x, y= map(int, input().split())
add = {}

for _ in range(x):
    site, ps = input().split()
    add[site] = ps

for _ in range(y):
    print(add[input().rstrip()])