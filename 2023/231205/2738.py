# 행렬 100 이하의 숫자인 A, B를 입력받자.
N, M = map(int, input().split())
if N > 100 or M > 100:
    print('N과 M은 100 이하의 숫자여야 합니다.')

# 행렬 A  
A = [list(map(int, input().split())) for t in range(N)]

# 행렬 B 
B = [list(map(int, input().split())) for t in range(N)]

# 결과 행렬 초기화
result = [[0] * M for t in range(N)]

# 행렬 A와 B를 더하여 결과 행렬에 저장
for i in range(N):
    for j in range(M):
        result[i][j] = A[i][j] + B[i][j]

# 결과 출력
for row in result:
    print(" ".join(map(str, row)))
