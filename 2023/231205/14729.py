# sys 모듈을 import하고, sys.stdin.readline을 input으로 사용
import sys 
input = sys.stdin.readline

# N에 정수를 입력받음
N = int(input())

# 입력된 N이 특정 범위에 속하는지 확인하고 아니라면 오류 메시지 출력
if 8 > N or N > 10000000:
    print('8 ≤ N ≤ 10,000,000 범위의 수를 입력할 것')

# 처음 7개의 실수를 입력받아 리스트로 저장하고 정렬
result = [float(input()) for i in range(7)]
result.sort()

# 이후 (N-7)번만큼 입력을 받아서 리스트에 추가하고 정렬
for i in range(N-7):
    result.append(float(input()))
    result.sort()
    result.pop()  # 가장 작은 값 삭제

# 결과 출력
for i in result:
    # 각 숫자를 소수점 아래 3자리까지 표시하고 출력
    print('{:.3f}'.format(i))

# 시간초과로 오답이 된 것
# 학생 수 입력
N = int(input())

# 성적을 저장할 리스트 초기화
grades = []

# 성적 입력 받기
for a in range(N):
    grade = float(input())
    grades.append(grade)

# 성적을 낮은 순으로 정렬
sorted_grades = sorted(grades)

# 하위 7명의 성적 출력
for i in range(7):
    print(sorted_grades[i])

