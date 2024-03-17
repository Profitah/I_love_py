N = int(input())
cnt = 666
while N != 0:
    if '666' in str(cnt): 
        N = N-1
        if N == 0:
            break
    cnt = cnt + 1
print(cnt)