# 사용자로부터 숫자 n을 입력받음
n=int(input())

# 동적 계획법을 위한 2차원 리스트 초기화
d=[]

# n번 반복하면서
for i in range(n):
  # 사용자로부터 입력받은 숫자들을 2차원 리스트에 추가
  d.append(list(map(int, input().split())))

# 첫 번째 줄을 제외한 각 줄에 대해
for i in range(1,n):
  # 각 줄의 각 숫자에 대해
  for j in range(len(d[i])):
    # 만약 첫 번째 숫자라면
    if j==0:
      # 현재 숫자에 윗줄의 같은 위치의 숫자를 더함
      d[i][j]=d[i][j]+d[i-1][j]
    # 만약 마지막 숫자라면
    elif j==len(d[i])-1: 
      # 현재 숫자에 윗줄의 왼쪽 위치의 숫자를 더함
      d[i][j]=d[i][j]+d[i-1][j-1]
    # 그 외의 경우
    else:
      # 현재 숫자에 윗줄의 왼쪽 위치의 숫자와 같은 위치의 숫자 중 큰 숫자를 더함
      d[i][j]=max(d[i-1][j-1],d[i-1][j])+d[i][j]

# 마지막 줄의 가장 큰 숫자를 출력
print(max(d[n-1]))
