# 사용자로부터 정수 N을 입력받음
N = int(input())

# 사용자로부터 N개의 정수를 입력받아 리스트 A에 저장
A = list(map(int, input().split()))

# 리스트 A의 최솟값과 최댓값을 출력
print(min(A), max(A))
