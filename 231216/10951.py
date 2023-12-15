# 무한 반복
while True:
    try:
        # 한 줄을 입력받아 user_input에 저장
        user_input = input()

        # 입력이 없으면 반복문 종료
        if not user_input:
            break

        # 입력값을 공백을 기준으로 나누고 정수로 변환하여 a와 b에 저장
        a, b = map(int, user_input.split())

        # A와 B를 더한 결과를 출력
        print(a + b)

    # EOFError 예외가 발생하면 반복문 종료
    except EOFError:
        break
