def prime(num):
    # num이 2보다 작으면 False를 반환합니다.
    if num < 2:
        return False
    # 2부터 int(num**0.5) + 1까지의 수 중에서 나누어지는 수가 있는지 검사합니다.
    for i in range(2, int(num**0.5) + 1):
        # num이 i로 나누어지면 False를 반환합니다.
        if num % i == 0:
            return False
    # 나누어지는 수가 없으면 True를 반환합니다.
    return True

# M과 N 값을 입력받습니다.
M, N = map(int, input().split())

# M부터 N까지의 수 중에서 소수인 수를 출력합니다.
for i in range(M, N + 1):
    if prime(i):
        print(i)
