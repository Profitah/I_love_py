import itertools
import math

r_, c_ = map(int, input().split())
d = [tuple(map(int, input().split())) for _ in range(3)]

d.sort()
ans = float('inf')

for permuted_d in itertools.permutations(d):
    cur = 0
    r, c = r_, c_
    for nr, nc in permuted_d:
        cur += math.sqrt((r - nr) ** 2 + (c - nc) ** 2)
        r, c = nr, nc
    ans = min(ans, cur)

print(int(ans))
