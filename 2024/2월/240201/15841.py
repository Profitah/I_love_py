def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        prev_fib, curr_fib = 0, 1
        for _ in range(2, n+1):
            prev_fib, curr_fib = curr_fib, prev_fib + curr_fib
        return curr_fib


import sys

for line in sys.stdin:
    if (hour:=int(line)) == -1:
        break
    print(f"Hour {hour}: {fibonacci(hour)} cow(s) affected")
