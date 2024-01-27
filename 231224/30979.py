T = int(input())
N = int(input())

F_values = list(map(int, input().split()))

for F in F_values:
    T -= F

print("Padaeng_i", end=' ')

if T > 0:
    print("Cry")
else:
    print("Happy")
