import sys

input = sys.stdin.readline

N, M = map(int, input().split())

arr = dict()
ans = []
for i in range(N):
    x = input()
    if x not in arr:
        arr[x] = i

for i in range(M):
    y = input()
    if y in arr:
        ans.append(y)
        
ans.sort()
print(len(ans))
print(''.join(ans), end = '')