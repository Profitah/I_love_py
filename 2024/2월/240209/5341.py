while True:
    sum = 0
    x = int(input())
    if not x:
        break
    for _ in range(1, x+1):
        sum += _
    print(sum)