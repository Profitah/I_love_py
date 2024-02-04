HGAP = 3
WGAP = 8

def debug(test):
    for row in test:
        print(''.join(row))

def solve(test, h, w):
    a = int(test[h + 1][w + 1])
    b = int(test[h + 1][w + 3])
    c = int(test[h + 1][w + 5])
    if test[h + 1][w + 6] != '.':
        c *= 10
        c += int(test[h + 1][w + 6])

    if a + b == c:
        length = 7 if c >= 10 else 6
        test[h + 1][w] = '*'
        test[h + 1][w + length] = '*'
        for i in range(1, length):
            test[h][w + i] = '*'
            test[h + 2][w + i] = '*'
    else:
        for i in range(3):
            test[h + i][w + 3 - i] = '/'

N, M = map(int, input().split())

N *= HGAP
M *= WGAP

test = [[''] * M for _ in range(N)]

for h in range(N):
    line = input()
    for w in range(M):
        test[h][w] = line[w]

for h in range(0, N, HGAP):
    for w in range(0, M, WGAP):
        solve(test, h, w)

debug(test)
