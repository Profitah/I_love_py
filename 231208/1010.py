import sys
input = sys.stdin.readline

def bridge(n, m):
    # 동적 계획법을 위한 2차원 리스트 초기화
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

    # 초기값 설정
    for i in range(1, m+1):
        dp[1][i] = i

    # 동적 계획법을 이용한 풀이
    for j in range(2, n+1):
        for k in range(j, m+1):
            for l in range(k, j-1, -1):
                dp[j][k] += dp[j-1][l-1]

    return dp[n][m]

# 테스트 케이스의 개수 T 입력
T = int(input().rstrip())

# 각 테스트 케이스에 대해 다리의 개수 계산 및 출력
for _ in range(T):
    n, m = map(int, input().rstrip().split())
    print(bridge(n, m))
