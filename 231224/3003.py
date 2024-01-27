# 기준 체스말의 개수를 나타내는 리스트 c를 정의합니다.
c = [1, 1, 2, 2, 2, 8]

# 입력을 받아 리스트 input으로 저장합니다.
input = list(map(int, input().split()))

# c 리스트의 길이만큼 반복하면서 결과를 출력합니다.
for i in range(len(c)):
    # c[i]에서 input[i]를 뺀 값을 출력하고, 띄어쓰기로 구분하여 출력합니다.
    print(c[i] - input[i], end=' ')
