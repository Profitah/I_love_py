n = int(input())

xmap = {}
ymap = {}
cows = []

for _ in range(n):
    x, y = map(int, input().split())
    cows.append([x, y])

    xmap[x] = xmap.get(x, 0) + 1
    ymap[y] = ymap.get(y, 0) + 1

arr = [[0, 0] for _ in range(3)]
for i in range(3):
    xMaxEntry = max(xmap.items(), key=lambda x: x[1], default=(None, None))
    yMaxEntry = max(ymap.items(), key=lambda x: x[1], default=(None, None))

    if xMaxEntry[1] >= yMaxEntry[1]:
        arr[i][0] = 0
        arr[i][1] = xMaxEntry[0]
        del xmap[xMaxEntry[0]]
    else:
        arr[i][0] = 1
        arr[i][1] = yMaxEntry[0]
        del ymap[yMaxEntry[0]]

result = True

for x, y in cows:
    if not ((arr[0][0] == 0 and x == arr[0][1]) or (arr[1][0] == 0 and x == arr[1][1]) or (arr[2][0] == 0 and x == arr[2][1]) or (arr[0][0] == 1 and y == arr[0][1]) or (arr[1][0] == 1 and y == arr[1][1]) or (arr[2][0] == 1 and y == arr[2][1])):
        result = False
        break

print(1 if result else 0)
