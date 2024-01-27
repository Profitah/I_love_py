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
        # 입력된 문자열을 공백을 기준으로 나누어 리스트로 만든 후, 나이를 정수로 변환
        age, name = map(str, sys.stdin.readline().split())
        # age가 1 이상 200 이하인지 확인
        if 1 <= int(age) <= 200:
            break
        else:
            print('나이는 1 이상 200 이하의 정수여야 합니다.')

    # 나이와 이름을 튜플로 만들어 리스트에 추가
    mylist.append((int(age), name))

# 나이를 기준으로 정렬
mylist.sort(key=lambda x: x[0])

# 결과값을 출력
for result in mylist:
    print(result[0], result[1])
