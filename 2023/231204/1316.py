# 지피티와 협업 a
# 단어의 개수 N을 입력받음
N = int(input())

# 그룹 단어의 개수를 저장할 변수 count 초기화
count = 0

# N개의 단어에 대해 반복
for i in range(N):
    word = input().strip()  # 공백 제거를 통해 입력 받음

    # 각 문자가 연속해서 나타나는지를 확인
    group_word = True
    for i in range(len(word)-1):
        if word[i] != word[i+1] and word[i] in word[i+1:]:
            group_word = False
            break

    # 그룹 단어인 경우 count 증가
    if group_word:
        count += 1

# 결과 출력
print(count)

# 돌아다니다 주움 b
# 입력으로 단어의 개수 N을 받음
N = int(input())

# 그룹 단어의 개수를 세는 변수 cnt를 N으로 초기화
cnt = N

# N개의 단어에 대해 반복
for i in range(N):
    # 각 단어를 입력받음
    word = input()
    
    # 단어의 길이만큼 반복
    for j in range(0, len(word)-1):
        # 현재 문자와 다음 문자가 같을 경우, 넘어감
        if word[j] == word[j+1]:
            pass
        # 현재 문자가 이후 문자열에 존재하는 경우, 그룹 단어가 아님
        elif word[j] in word[j+1:]:
            # 그룹 단어의 개수를 줄이고 반복문 탈출
            cnt -= 1
            break

# 최종적으로 그룹 단어의 개수를 출력
print(cnt)

