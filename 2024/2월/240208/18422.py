def count_rectangles(N, M, picture):
    count = 0
    for i in range(N):
        for j in range(M):
            if picture[i][j] == '*':
                if (i == 0 or picture[i-1][j] != '*') and (j == 0 or picture[i][j-1] != '*'):
                    count += 1
    return count

N, M = map(int, input().split())
picture = [input() for _ in range(N)]
result = count_rectangles(N, M, picture)
print(result)
