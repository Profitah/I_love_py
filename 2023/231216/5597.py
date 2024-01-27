# 입력값 받기
x = [int(input()) for _ in range(28)]

# 1부터 30까지의 숫자 집합 만들기
numbers = set(range(1, 31))

# 입력받은 값으로 set 만들기
user_input = set(x)

# 차집합을 이용해 빠진 번호 찾기
n = numbers - user_input

# 결과 출력
print(min(n))
print(max(n))
