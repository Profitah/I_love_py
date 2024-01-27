#30501.py

# 사용자로부터 반복 횟수 입력 받기
for i in range(int(input())):
    # 각 반복에서 문자열 입력 받기
    a = input()
    
    # 입력된 문자열에 'S'가 포함되어 있는지 확인
    if 'S' in a:
        # 'S'가 포함되어 있으면 해당 문자열 출력
        print(a)
