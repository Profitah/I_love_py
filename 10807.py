# 정수 N 입력
N = int(input())  # 정수의 개수 (1 <= N <= 100)

# N개의 정수를 공백을 기준으로 나눠 리스트로 받음
numbers = list(map(int, input().split()))

# 찾으려는 정수 v 입력
v = int(input())  # -100 <= v <= 100

# 리스트에서 정수 v의 개수를 세고 출력
count_of_v = numbers.count(v)
print(count_of_v)
