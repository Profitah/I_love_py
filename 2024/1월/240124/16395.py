from sys import stdin

x, y = map(int, stdin.readline().split())

dp = [[0] * (x+1) for _ in range(x+1)]
dp[1][1] = 1

for i in range(2, x+1):
    for j in range(1, i+1):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

print(dp[x][y])
