try:
    # x와 y를 입력받음
    x, y = map(int, input().split())

    # 입력받은 숫자들을 저장할 리스트
    a_list = list(map(int, input().split()))
    
    # a_list의 각 숫자가 y보다 작으면 출력
    for num in a_list:
        if num < y:
            print(num, end=' ')

except ValueError:
    print("올바른 숫자를 입력하세요.")
