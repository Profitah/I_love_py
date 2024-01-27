def counts(n):
    # n이 1일 경우 1을 반환합니다.
    if n == 1:
        return 1
    # n이 2일 경우 2를 반환합니다.
    elif n == 2:
        return 2
    # n이 3일 경우 4를 반환합니다.
    elif n == 3:
        return 4

    # dp 리스트를 생성하고 초기값을 설정합니다.
    dp = [0] * (n + 1)
    dp[1], dp[2], dp[3] = 1, 2, 4

    # dp[i]를 구하기 위해 반복문을 실행합니다.
    for i in range(4, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

    # dp[n]을 반환합니다.
    return dp[n]

# 테스트 케이스의 개수 T를 입력받습니다.
T = int(input()) 

# T만큼 반복하면서 n을 입력받고 counts 함수를 호출하여 결과를 출력합니다.
for _ in range(T):
    n = int(input())
    result = counts(n)
    print(result)
