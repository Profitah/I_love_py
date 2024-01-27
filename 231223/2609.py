a, b = map(int, input().split())

def gcd(a, b):
    # 유클리드 호제법을 사용하여 최대공약수를 계산
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    # 최소공배수를 계산합니다.
    return a * b // gcd(a, b)

# 입력받은 a와 b의 최대공약수를 계산하고 출력
print(gcd(a, b))

# 입력받은 a와 b의 최소공배수를 계산하고 출력
print(lcm(a, b))
