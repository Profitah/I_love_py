# for문 사용시 sys.stdin.readline를 사용하면 시간초과오류를 예방할 수 있다고 함

# sys 모듈을 import
import sys

# 테스트 케이스의 개수 T
T = int(sys.stdin.readline())
# T를 입력받을 때 범위를 확인하는 while 루프 추가
while not (1 <= T <= 1000000):
    print('1이상 1000000 이하 범위의 수를 입력하세요.')
    T = int(sys.stdin.readline())

# 결과값을 저장할 리스트 초기화
mylist = []

# T만큼 반복
for i in range(T):
    # a, b를 입력받을 때 범위를 확인하는 while 루프를 추가
    while True:
        # 입력된 문자열을 공백을 기준으로 나누어 리스트로 만든 후, 첫 번째 값을 정수로 변환
        a, b = map(int, sys.stdin.readline().split())
        # a와 b가 1 이상 1000 이하인지 확인
        if 1 <= a <= 1000 and 1 <= b <= 1000:
            break
        else:
            print('각 정수는 1 이상 1000 이하의 수여야 합니다.')

    # 결과값을 리스트에 추가
    mylist.append(a + b)

# 모든 결과값을 출력
for result in mylist:
    print(result)
