N = int(input())
Mynum = 0

for i in range(-N, N+1):
    if i == 0:
        Mynum += (N * 2 + 1) ** 2
    elif a < 0:
        Mynum += N + (N + i)
    else:
        Mynum += N + (N - i + 2)

print(Mynum)
