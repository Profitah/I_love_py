N = int(input())

if N < 10:
    N *= 10

temp = N
cnt = 0

while True:
    cnt += 1
    temp = temp % 10 * 10 + (temp // 10 + temp % 10) % 10

    if temp == N:
        break

print(cnt)
