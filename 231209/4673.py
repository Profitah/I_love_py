# 1부터 10,000까지의 숫자 리스트 생성
numbers = list(range(1, 10_001))
remove_list = []  # 생성자가 있는 숫자를 저장할 리스트

# 생성자가 있는 숫자 찾기
for num in numbers:
    temp = num
    for n in str(num):
        temp += int(n)  # 각 자리수의 숫자를 더함
    if temp <= 10_000:  # 10,000보다 작거나 같을 때만 추가
        remove_list.append(temp)

# 중복값 제거
unique_remove_list = set(remove_list)

# 생성자가 있는 숫자를 삭제한 리스트
result_numbers = [num for num in numbers if num not in unique_remove_list]

# 결과 출력
for self_num in result_numbers:
    print(self_num)
