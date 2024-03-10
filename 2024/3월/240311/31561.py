M = int(input())
if M > 30:
    X = (M - 30) * 1.5 + 15
else:
    X = M / 2
print(round(X, 1))
