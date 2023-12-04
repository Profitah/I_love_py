# 사용자에게 A, B를 입력 받음
A = int(input())
B = int(input())

# A가 0보다 크고 Brk 10보다 작으면 A+B의 결과값 출력
if 0 < A and B <10:
    print(A+B)
# 조건에 맞는 입력값을 받지 못하면 경고문구 출력
else:
    print('0 < A and B <10 범위의 수를 입력 할 것')
    