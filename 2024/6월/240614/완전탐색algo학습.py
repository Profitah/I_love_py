# 백준 nal짜 ge산
# 완전탐색(브루트포스) 알고리즘을 이용한 풀이

def ESM_Check():
    E, S, M = map(int, input().split())  

    YearCheck = 1
    while True:
        # 순차적으로 조건을 만족하는 연도 찾기
        # E, S, M 값이 각각 15, 28, 19로 나누어 떨어질 때 해당 연도를 출력하고 반복을 종료.
        if (YearCheck - E) % 15 == 0 and (YearCheck - S) % 28 == 0 and (YearCheck - M) % 19 == 0: 
            print(YearCheck)
            break
        YearCheck += 1

ESM_Check()
