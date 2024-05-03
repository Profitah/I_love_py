n, m = map(int, input().split())
arr = [0] * 101

for _ in range(m):
    a, b, c = map(int, input().split())
    for k in range(a, b + 1):
        arr[k] = c

for i in range(1, n + 1):
    print(arr[i], end=' ')
