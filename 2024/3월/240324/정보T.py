import sys

def solve():
    n = int(sys.stdin.readline())
    a = [[0] * 5 for _ in range(n)]
    
    for i in range(n):
        v = list(map(int, sys.stdin.readline().split()))
        for j in range(5):
            if v[j]:
                a[i][j] = 1

    ans = (-1, -1)
    ans_mx = -1
    
    for i in range(5):
        for j in range(i + 1, 5):
            cnt = sum(1 for k in range(n) if a[k][i] and a[k][j])
            if cnt > ans_mx:
                ans_mx = cnt
                ans = (i, j)
    
    print(ans_mx)
    for i in range(5):
        if i == ans[0] or i == ans[1]:
            print(1, end=' ')
        else:
            print(0, end=' ')

solve()
