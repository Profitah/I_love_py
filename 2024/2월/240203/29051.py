c = [2, 1, 1, 1, 2, 2, 1, 3, 3, 2, 3, 1, 1, 1, 1, 1, 1, 2, 1, 2, 1, 1, 1, 2, 2, 1]

a = 0
s = input().upper()

for i in s:
    a += c[ord(i) - ord('A')]

print(a)