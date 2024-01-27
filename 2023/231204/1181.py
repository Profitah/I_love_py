#구글링..

# 수의 개수 N을 입력받음
n = int(input())

# N의 범위 확인
if not (1 <= n <= 1000000):
    print("1 <= N <= 1000000 범위의 정수만 입력해주세요")
else:
    # 수를 입력받아 리스트에 저장
    lst = [input().strip() for _ in range(n)]

    # 중복 제거를 위해 집합(set)을 사용
    set_lst = set(lst)

    # 다시 리스트로 변환하고 정렬
    lst = list(set_lst)
    lst.sort()

    # 길이에 따라 정렬
    lst.sort(key=len)

    # 결과 출력
    for i in lst:
        print(i)
