#답 a 
# 사용자로부터 영어 소문자와 대문자로 이루어진 단어를 입력받음
x = input()

# 문자열의 대소문자를 바꾸어 새로운 문자열에 저장
result = x.swapcase()

# 결과 출력
print(result)

#답 b
#if문과 for문을 이용한 해결
# 단어 입력
x = input()

# 대문자는 소문자로, 소문자는 대문자로 변환하여 출력
result = '' # 결과값을 담기 위해 비어있는 상태여야 함
for char in x :
    if char.isupper():  # 대문자인 경우
        result += char.lower()  # 소문자로 변환하여 추가
    elif char.islower():  # 소문자인 경우
        result += char.upper()  # 대문자로 변환하여 추가
    else:
        result += char  # 알파벳이 아닌 경우 그대로 추가

print(result)
