x_values = []
y_values = []

for _ in range(int(input())) :
    x, y = map(int, input().split())
    x_values.append(x)
    y_values.append(y)

width = max(x_values) - min(x_values)
height = max(y_values) - min(y_values)
area = width * height

print(area)
