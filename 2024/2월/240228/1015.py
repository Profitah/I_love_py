import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

s_arr = sorted(arr)

p = []
for i in arr:
    p.append(s_arr.index(i))
    s_arr[s_arr.index(i)] = -1

for r in p:
    sys.stdout.write(str(r)+' ')
