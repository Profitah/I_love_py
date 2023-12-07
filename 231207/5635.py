# a. 왜 오답인지 모르겠음
# 유효성 검사를 위한 함수 정의
def valid(name, day, month, year):
    # 이름 길이 확인
    if not 0 < len(name) <= 15:  # 이름 길이가 1글자 이상, 15글자 이하여야 함
        return False
    # 생일 연도 범위 확인
    if not 1990 <= int(year) <= 2010:
        return False
    # 생일 월 범위 확인
    if not 1 <= int(month) <= 12:
        return False
    # 생일 일 범위 확인
    if not 1 <= int(day) <= 31:
        return False
    return True

# 학생 정보를 입력받을 리스트 생성
students = []

# 반에 있는 학생의 수 n. (1 ≤ n ≤ 100)
while True:
    n = int(input("반에 있는 학생의 수를 입력하세요 (1 ≤ n ≤ 100): "))
    if 1 <= n <= 100:
        break
    else:
        print('1 ≤ n ≤ 100 범위의 수를 입력하세요.')

# 학생 정보 입력 받기
for i in range(n):
    name, day, month, year = input().split()
    if not valid(name, day, month, year):
        print('조건을 충족하지 않는 입력입니다. 다시 확인해주세요:', name, day, month, year)
        exit()

    students.append((name, int(day), int(month), int(year)))

# 가장 어린 나이와 가장 많은 나이를 찾아 출력
def find_age_extremes(students):
    min_age = 0
    max_age = 0

    for i in range(1, len(students)):
        if students[i][3] > students[min_age][3]:  
            min_age = i
        if students[i][3] < students[max_age][3]:
            max_age = i

    return students[min_age][0], students[max_age][0]

# 가장 어린 나이와 가장 많은 나이를 찾아 출력
youngest, oldest = find_age_extremes(students)
print(youngest)
print(oldest)

#b. 구글링으로 맞춰버림...
import sys
input = sys.stdin.readline

lst = []
# 학생 수 입력 받기
for _ in range(int(input())):
    n, d, m, y = input().rstrip().split()
    # 정수로 변환
    d, m, y = map(int, (d, m, y))
    # 학생 정보 리스트에 추가
    lst.append((y, m, d, n))

# 학생 정보를 생년월일 기준으로 정렬
lst.sort()

# 출력: 가장 어린 학생과 가장 나이 많은 학생의 이름 출력
print(lst[-1][3])  # 가장 어린 학생
print(lst[0][3])   # 가장 나이 많은 학생

