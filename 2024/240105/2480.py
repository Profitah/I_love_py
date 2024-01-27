# 세 개의 숫자를 입력 받음
n = list(map(int, input().split()))

# 모든 숫자가 동일한 경우
if n.count(n[0]) == 3:
    print(10000 + n[0] * 1000)
# 두 숫자가 동일한 경우
elif n.count(n[0]) == 2:
    print(1000 + n[0] * 100)
# 세 번째 숫자가 동일한 경우
elif n.count(n[1]) == 2:
    print(1000 + n[1] * 100)
# 나머지 경우
elif n.count(n[2]) == 2:
    print(1000 + n[2] * 100)
# 모든 숫자가 다른 경우
else:
    print(100 * max(n))
