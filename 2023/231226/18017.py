# 입력 받기
a, b = map(float, input().split())

# 상수 정의
c = 299792458

# 계산 및 결과 출력
res = (a + b) / (1 + (a * b) / (c ** 2))
print("{:.2f}".format(res))
