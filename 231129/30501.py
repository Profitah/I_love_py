#아마도 질문게시판 참고

# 사용자로부터 정수를 입력받아 그 수만큼 반복
for i in range(int(input())):
    # 사용자로부터 문자열을 입력받아 변수 a에 저장
    a = input()
    
    # 만약 문자열 a에 'S'가 포함되어 있다면 문자열 a를 출력
    if 'S' in a:
        print(a)
