# 진호의 MBTI 유형 입력
mbti = input()

# 진호의 친구 수 입력
n = int(input())  # 1 이상 100 이하의 자연수

# 친구들의 MBTI 유형을 저장할 리스트
friends = [input() for i in range(n)]

# 진호와 MBTI 유형이 같은 사람의 수 계산
matching = friends.count(mbti)

# 결과 출력
print(matching)
