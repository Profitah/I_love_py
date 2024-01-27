#오답(출력형식 신경쓰지 않음)
# 사용자로부터 int 형식으로 숫자 입력받기
N = int(input())

# 각 자리 숫자를 리스트로 만들기
mylist = list(map(int, str(N)))

# 리스트를 내림차순으로 정렬
mylist.sort(reverse=True)

# 정렬된 리스트 출력
print(mylist)

#출력형식을 수정한 정답
# 사용자로부터 int 형식으로 숫자 입력받기
N = int(input())

# 각 자리 숫자를 리스트로 만들기
mylist = list(map(int, str(N)))

# 리스트를 내림차순으로 정렬
mylist.sort(reverse=True)

# 정렬된 리스트를 문자열로 변환하여 출력
result = ''.join(map(str, mylist))
print(result)
