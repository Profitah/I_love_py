# 학교이름 출력 횟수 T를 입력받는다
T = int(input())

# T에 맞는 처리 반복
for _ in range(T):
    N = int(input()) # 학교 개수

    # 학교 정보를 담을 리스트 생성
    school_info = []
    for _ in range(N): # N에 맞는 처리 반복
        name, amount = input().split() # 학교명과 술을 마신 횟수를 한 줄에 차례대로 입력받음
        school_info.append((name, int(amount))) # 입력받은 학교명과 술을 마신횟수를 학교정보 리스트에 추가

    # 술을 가장 많이 마신 학교 찾기
    max_school_info = max(school_info, key=lambda x: x[1])

    # 결과값 출력
    print(max_school_info[0])  # 튜플에서 학교 이름을 가져와 출력
