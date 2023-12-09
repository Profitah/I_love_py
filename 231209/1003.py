def fib(N):
    # 초기값 설정
    zeros = [1, 0, 1]  # 0이 출력되는 횟수 리스트
    ones = [0, 1, 1]   # 1이 출력되는 횟수 리스트

    # N이 3 이상일 때, 피보나치 수열 계산
    if N >= 3:
        for i in range(2, N):
            zeros.append(zeros[i - 1] + zeros[i])
            ones.append(ones[i - 1] + ones[i])

    # 결과 출력
    print(f"{zeros[N]} {ones[N]}")

# 테스트 케이스 수 입력
T = int(input())
for _ in range(T):
    # 각 테스트 케이스에 대해 N 입력 및 함수 호출
    N = int(input())
    fib(N)
