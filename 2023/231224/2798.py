# N과 M을 입력받아서 변수에 저장합니다.
N, M = map(int, input().split())

# 정렬된 숫자 리스트를 입력받아서 변수에 저장합니다.
lst = sorted(map(int, input().split()))

# 최대 합을 저장할 변수를 초기화합니다.
max_sum = 0

# lst 리스트의 각 요소와 인덱스에 대해 반복합니다.
for i, a in enumerate(lst):
    # i+1 인덱스부터 끝까지의 요소에 대해 반복합니다.
    for j, b in enumerate(lst[i+1:], i+1):
        # j+1 인덱스부터 끝까지의 요소에 대해 반복합니다.
        for c in lst[j+1:]:
            # 세 요소의 합을 계산합니다.
            three_sum = a + b + c
            # 세 요소의 합이 M보다 작거나 같은 경우에만 최대 합을 갱신합니다.
            if three_sum <= M:
                max_sum = max(max_sum, three_sum)
            else:
                # 세 요소의 합이 M을 초과하는 경우 반복문을 종료합니다.
                break

# 최대 합을 출력합니다.
print(max_sum)
