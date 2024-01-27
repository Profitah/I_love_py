import sys

# 수의 개수 N을 입력받음
N = int(sys.stdin.readline().strip())

# N의 범위 확인
if not (1 <= N <= 1000000):
    print("1 <= N <= 1000000 범위의 정수만 입력해주세요")
else:
    # 수를 입력받아 리스트에 저장
    numbers = [int(sys.stdin.readline().strip()) for _ in range(N)]

    # 입력된 수의 개수가 N과 일치하는지 확인한 뒤 리스트를 오름차순으로 정렬
    if len(numbers) == N:
        numbers.sort()

        # 정렬된 수 한 줄에 하나씩 출력
        for num in numbers:
            print(num)
    else:
        print("입력 할 수 있는 숫자 조건을 확인해 주세요.")
