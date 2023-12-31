# https://www.youtube.com/watch?v=wwqS53DPMw0 보고 배움

n = int(input())
A = list(map(int, input().split()))
A.sort()  # 이분탐색을 하려면 정렬되어야 함
m = int(input())
B = list(map(int, input().split()))


def binary_search(target, array):  # 0
    current_min = 0  # 현재 최소의 인덱스
    current_max = n - 1  # 현재 최대의 인덱스
    cursor = (current_min + current_max) // 2  # 현재 커서

    while current_min <= current_max:
        if array[cursor] == target:  # 수정된 부분
            return 1  # 찾았다면 1을 리턴
        elif array[cursor] < target:
            current_min = cursor + 1  # 최소 인덱스를 커서보다 1 증가
        else:
            current_max = cursor - 1  # 최대 인덱스를 커서보다 1 감소
        cursor = (current_max + current_min) // 2  # 커서를 바꿔주고 반복문 돌게 함
    return 0  # 위를 충족하지 않으면 0 리턴

for i in range(m):
    print(binary_search(B[i], A))
