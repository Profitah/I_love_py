# 질문게시판 참고

# A와 B를 입력받음
A = int(input())
B = int(input())

# main 변수에 B 값을 복사
main = B

# B를 문자열로 변환하고 각 자릿수를 정수로 변환하여 리스트로 저장
B = list(str(B))
B = map(int, B)
B = list(B)

# 리스트 B에서 각 자릿수를 C, D, E 변수에 저장
C = B[0]
D = B[1]
E = B[2]

# A와 E를 곱한 결과 출력
print(A * E)
# A와 D를 곱한 결과 출력
print(A * D)
# A와 C를 곱한 결과 출력
print(A * C)
# A와 main을 곱한 결과 출력
print(A * main)
