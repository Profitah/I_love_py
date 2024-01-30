n = int(input())
l = 1

while n > l:
    n -= l
    l += 1

if l % 2 == 0:
    a, b = n, l - n + 1
else:
    a, b = l - n + 1, n

print(f'{a}/{b}')
