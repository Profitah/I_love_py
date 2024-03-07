import sys

N, K = map(int, sys.stdin.readline().split())

ad_spaces = []
for _ in range(N):
    A, B = map(int, sys.stdin.readline().split())
    ad_spaces.append((A, B))

differ = [B - A for A, B in ad_spaces]

differ.sort()

min_increase = max(0, differ[K - 1]) if K <= len(differ) else 0

print(min_increase)
