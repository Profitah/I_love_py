# 과목 수 입력
num_subjects = int(input())

# 각 과목의 시험 점수를 리스트로 입력받음
test_scores = list(map(int, input().split()))

# 시험 점수 중 최대값을 찾음
max_score = max(test_scores)

# 변환된 점수를 저장할 리스트 초기화
converted_scores = []

# 각 점수를 최대 점수로 나눈 후 100을 곱하여 새로운 점수 생성하여 리스트에 추가
for score in test_scores:
    converted_scores.append(score / max_score * 100)

# 변환된 점수의 평균 계산
average_score = sum(converted_scores) / num_subjects

# 결과 출력
print(average_score)
