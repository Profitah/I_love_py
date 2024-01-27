# 질문게시판에 있던 코드 참고함

# 빈 리스트 li 생성
li = []

# 7번 반복하여 사용자로부터 정수를 입력받고 리스트 li에 추가
for i in range(7):
    a = int(input())
    li.append(a)

# 홀수를 담을 빈 리스트 odd_li를 생성
odd_li = []

# 리스트 li를 순회하면서 홀수인 경우 odd_li에 추가
for i in li:
    if i % 2 == 1:
        odd_li.append(i)

# 만약 홀수를 담은 리스트 odd_li의 길이가 0이라면 -1을 출력
if len(odd_li) == 0:
    print(-1)
else:
    # 홀수의 합과 최솟값을 출력
    print(sum(odd_li))
    print(min(odd_li))


