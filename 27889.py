# 사용자로부터 학교 코드 입력 받기
x = input()

# 학교 코드에 따라 다른 학교 이름 출력
if x == 'NLCS':
    print('North London Collegiate School')
elif x == 'BHA':
    print('Branksome Hall Asia')
elif x == 'KIS':
    print('Korea International School')
else:
    # 입력된 코드가 어떤 학교에도 해당하지 않을 경우
    print('St. Johnsbury Academy')
