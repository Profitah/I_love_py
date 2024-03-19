import sys
input = sys.stdin.readline 

N = int(input())    

idx = 1
for i in range(1, N):
    if i % 2 != 0:  
        idx *= i

print(idx)  