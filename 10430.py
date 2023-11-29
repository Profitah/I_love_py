# 입력받은 숫자를 공백을 기준으로 나눠 리스트에 담은 뒤, 차례대로 a, b, c로 이름 붙였다.
A, B, C = map(int, input().split())

# 실행
print((A + B) % C)
print(((A % C) + (B % C)) % C)
print((A * B) % C)
print(((A % C) * (B % C)) % C)
