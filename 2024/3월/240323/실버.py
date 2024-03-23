def dfs(start, depth):
    global sb
    if depth == M:
        for i in range(M):
            sb += str(printArr[i]) + " "
        sb += "\n"
        return
    
    before = -1
    for i in range(start, N):
        now = arr[i]
        if before == now or isVisited[i]:
            continue
        else:
            before = now
            isVisited[i] = True
            printArr[depth] = arr[i]
            dfs(i + 1, depth + 1)
            isVisited[i] = False

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

printArr = [0] * M
isVisited = [False] * N
sb = ""

dfs(0, 0)
print(sb)
