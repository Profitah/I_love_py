from sys import stdin

def factorial(n):
    # n이 0인 경우 1을 반환
    if n == 0:
        return 1
    # n과 factorial(n-1)을 곱한 값을 반환
    return n * factorial(n-1)

# n과 k 값을 입력받기
n, k = map(int, stdin.readline().split())

# 이항 계수를 계산하여 출력
print(factorial(n) // (factorial(k) * factorial(n - k)))
