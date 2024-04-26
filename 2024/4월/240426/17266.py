n = int(input())
m = int(input())
positions = list(map(int, input().split()))
max_height = max(positions[0], n - positions[-1])

for i in range(1, m):
    distance = positions[i] - positions[i-1]
    if distance % 2 == 0:
        height = distance // 2
    else:
        height = (distance + 1) // 2
    max_height = max(max_height, height)

print(max_height)
