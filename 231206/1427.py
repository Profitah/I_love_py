# 오답이라고 함...ㅠㅠ
# 사용자로부터 int 형식으로 숫자 입력받기
N = int(input())

# 각 자리 숫자를 리스트로 만들기
mylist = list(map(int, str(N)))

# 리스트를 내림차순으로 정렬
mylist.sort(reverse=True)

# 정렬된 리스트 출력
print(mylist)

# 조건 검사
if N > 1000000000 or any(digit > 9 for digit in mylist):
    print('1000000000 이하의 정수를 입력하고, 각 자리 숫자는 0부터 9까지의 정수여야 합니다.')
