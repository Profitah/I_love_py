n = int(input())
B = list(map(int, input().split()))

A = []

current_sum = 0
for i in range(n):
    A_i = B[i] * (i + 1) - current_sum
    A.append(A_i)
    current_sum += A_i  

print(" ".join(map(str, A)))
