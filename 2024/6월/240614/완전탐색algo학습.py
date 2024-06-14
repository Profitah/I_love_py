def ESM_Check():
    E, S, M = map(int, input().split())  

    YearCheck = 1
    while True:
        # 완전탐색을 통해 가능한 모든 연도를 순차적으로 검사.
        if (YearCheck - E) % 15 == 0 and (YearCheck - S) % 28 == 0 and (YearCheck - M) % 19 == 0: # 15, 28, 19로 나누어 떨어지는 연도를 반복문을 통해 찾음.
            print(YearCheck)
            break
        YearCheck += 1

ESM_Check()
