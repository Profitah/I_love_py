# 사용자로부터 x와 y 좌표를 입력받아옴
x = int(input())
y = int(input())

# 주어진 좌표 (x, y)가 어느 사분면에 속하는지 판별하고 출력
# 1사분면: x와 y가 모두 양수인 경우 1 출력
if x > 0 and y > 0:
    print(1)

# 2사분면: x가 음수이고 y가 양수인 경우 2출력
elif x < 0 and y > 0:
    print(2)

# 3사분면: x와 y가 모두 음수인 경우 3출력
elif x < 0 and y < 0:
    print(3)

# 4사분면: x가 양수이고 y가 음수인 경우 4출력
else:
    print(4)
