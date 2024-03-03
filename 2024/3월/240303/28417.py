N = int(input())
r = 0

for _ in range(N):
    b = list(map(int, input().split()))
    m = max(b[:2])
    t = sorted(b[2:], reverse=True)

    s = m + sum(t[:2])
    r = max(r, s)

print(r)
