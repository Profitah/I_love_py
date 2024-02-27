N = int(input())
for _ in range(N, 0, -1):
    print(" " * (N-_) + "*" * (2*_-1))
for x in range(2,N+1):
    print(" " * (N-x) + "*" * (2*x-1))