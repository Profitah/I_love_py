while True:
    # 한 줄을 입력받아 공백을 기준으로 나누어 리스트로 변환
    inputs = list(map(int, input().split()))

    # 입력값이 [0, 0]이면 반복문 종료
    if inputs == [0, 0]:
        break

    # A와 B를 더한 결과 출력
    print(sum(inputs))
