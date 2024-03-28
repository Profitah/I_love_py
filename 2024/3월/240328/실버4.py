N, M  = map(int, input().split())
A = list(map(int, input().split()))

sum = A[0]
left = 0
right = 1
count = 0

while True:
    if sum < M:
        if right < N:
            sum += A[right]
            right += 1
        else:
            break
    elif sum == M:
        count += 1
        sum -= A[left]
        left += 1
    else:
        sum -= A[left]
        left += 1

print(count)