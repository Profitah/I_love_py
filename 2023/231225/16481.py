r1, r2, r3 = map(int, input().split())  # 세 개의 정수를 공백으로 구분하여 입력받음
result = (r1 * r2 * r3) / (r1 * r2 + r2 * r3 + r1 * r3)  # 계산 수행
print(f"{result:.10f}")  # 소수점 아래 10자리까지 출력
