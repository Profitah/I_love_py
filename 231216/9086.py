# 테스트 케이스 수 입력
t = int(input())

# 각 테스트 케이스에 대해 처리
for i in range(1, t + 1):
    # 문자열 입력
    user_input = input()
    
    # 입력된 문자열을 대문자로 변환
    x = user_input.upper()
    
    # 문자열의 첫 번째 문자
    y = x[0]
    
    # 문자열의 마지막 문자
    z = x[-1]
    
    # 결과 출력
    print(y, end="")
    print(z)
