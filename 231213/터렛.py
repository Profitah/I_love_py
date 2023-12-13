# 진호의 친구 수 입력
n = int(input())  # 1 이상 100 이하의 자연수

# 진호의 MBTI 유형 입력
myers_briggs_type = input()

# 친구들의 MBTI 유형을 저장할 리스트
friends_types = []

# 진호의 친구들의 MBTI 유형 입력
for _ in range(n):
    friend_type = input()
    friends_types.append(friend_type)

# 진호와 MBTI 유형이 같은 사람의 수 계산
matching_friends = friends_types.count(myers_briggs_type)

# 결과 출력
print(matching_friends)