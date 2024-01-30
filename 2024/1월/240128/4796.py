n = 0
while True:
    n += 1
    x, y, z = map(int, input().split())
    if x == 0 and y == 0 and z == 0:
        break
    a = z // y
    b = z % y
    if x < b:
        b = x
    c = a * x + b
    print("Case %d: %d" % (n, c))
