# 라운드의 수 입력
n = int(input())

# 초기 점수 설정
x = y = 100

# 각 라운드의 주사위 결과 처리
for _ in range(n):
    # 각 플레이어의 주사위 결과 입력
    a, b = map(int, input().split())

    # 주사위 결과에 따라 점수 갱신
    if a > b:
        y -= a
    elif a < b:
        x -= b

# 최종 점수 출력
print(x)
print(y)
