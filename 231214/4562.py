# x 입력
x = int(input())

# x번 만큼
for i in range(x):
    n, m = map(int, input().split()) # N, M을 입력받고 

# n이 m 보다 작으면 노브레인
    if n < m:
        print("NO BRAINS") 

        # n이 m 보다 크면 mmm 브레인
    else:
        print("MMM BRAINS")