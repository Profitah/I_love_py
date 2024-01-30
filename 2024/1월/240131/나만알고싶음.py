# 입력 받기
N = int(input())
f = list(map(int, input().split()))  # 첫째 날 
s = list(map(int, input().split()))  # 둘째 날 

# 0번째 인덱스에 0 삽입
f.insert(0, 0)
s.insert(0, 0)

# 동적 계획법을 위한 dp 테이블 초기화
dp = [0] * (N + 1)

# 모든 쓰레기에 대해 순회
for i in range(1, N + 1):
    mv = 0  # 최대값 저장 변수
    for j in range(1, N + 1):
        # 첫째 날 쓰레기가 둘째 날 쓰레기보다 작은 경우, 최대값 갱신
        if mv < dp[j] and f[i] > s[j]:
            mv = dp[j]
        # 첫째 날과 둘째 날 쓰레기 크기가 같은 경우, dp 테이블 갱신
        if f[i] == s[j]:
            dp[j] = mv + 1

# 가장 큰 값을 출력
print(max(dp))
