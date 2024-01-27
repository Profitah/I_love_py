# 정수 x를 입력받음
x = int(input())

# 2의 x 제곱을 계산하여 결과를 변수에 저장
result = 2 ** x

# 결과의 자릿수가 4300 이하인 경우에만 출력
if len(str(result)) <= 4300:
    print(result)
