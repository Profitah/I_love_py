# 정수 N을 입력받음
N = int(input())

# 입력 범위를 확인하고 경고 메시지 출력
if N < 0 or N > 500:
    print("N < 0 or N > 500 범위의 수를 입력할 것")
else:
    # 팩토리얼의 결과를 저장할 변수
    result = 1

    # 팩토리얼 계산
    for i in range(1, N + 1):
        result *= i

    # 팩토리얼 결과에서 끝의 0의 개수를 세는 변수
    zero_count = 0

    # 팩토리얼 결과에서 끝의 0의 개수를 세는 과정
    while result % 10 == 0:
        result //= 10
        zero_count+= 1

    # 결과 출력
    print(zero_count)
