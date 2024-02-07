n, m = map(int, input().split())
p = [input() for _ in range(n)]

rectangles = 0

for i in range(n):
    for j in range(m):
        if p[i][j] == '*':
            if i == 0 or p[i-1][j] != '*' or j == 0 or p[i][j-1] != '*':
                rectangles += 1

print(rectangles)
