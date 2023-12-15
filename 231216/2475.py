def verify(nums):
    # 숫자들을 제곱한 값들의 합을 계산
    total = sum(int(x) ** 2 for x in nums)

    # 10으로 나눈 나머지를 반환
    return total % 10

# 입력 받기
numbers = input().split()

# 함수 호출하여 검증수 출력
verification_number = verify(numbers)
print(verification_number)
