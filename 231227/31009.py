N = int(input())
jinju = 0
cnt = 0
arr = [0] * 1010

for i in range(N):
    s, cost = input().split()
    cost = int(cost)

    if s == "jinju":
        jinju = cost

    arr[i] = cost

for i in range(N):
    if arr[i] > jinju:
        cnt += 1

print(jinju)
print(cnt)
