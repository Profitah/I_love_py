N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

C = [0] * (max(max(A), max(B)) + 1)

for x in A:
    C[x] += 1

M = 0

for x in B:
    if x <= N and C[x] > 0:
        C[x] -= 1
        M += 1

print(M)
