import sys
input = sys.stdin.readline

number = int(input().strip())
factorial_values = [0] * 21
factorial_values[0] = 1
for i in range(1, 20):
    factorial_values[i] = i * factorial_values[i-1]

if number == 0:
    print("NO")
else:
    for i in range(20, -1, -1):
        if number >= factorial_values[i]:
            number -= factorial_values[i]

    if number == 0:
        print("YES")
    else:
        print("NO")
