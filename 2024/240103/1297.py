d, h, w = map(int, input().split())
ratio = d / (h**2 + w**2)**0.5

result_height = int(h * ratio)
result_width = int(w * ratio)

print(result_height, result_width)
