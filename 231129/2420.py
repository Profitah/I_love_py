#한 줄에 정수 2개를 입력 받고 빈칸을 기준으로 배열 n, m에 나누어 담음
n, m = map(int, input().split())

# 유명도의 차이를 계산
#n이 m보다 작을 경우 n - m 으로 차이를 구함
if n>=m:
    print(n-m)
#m이 n보다 작을 경우 m - n 으로 차이를 구함
else:
    print(m-n)