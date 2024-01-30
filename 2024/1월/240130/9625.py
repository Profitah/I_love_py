def fibonacci(n):
    if n <= 1:
        return (n, 0)
    else:
        (prev, current) = fibonacci(n - 1)
        return (prev + current, prev)

K = int(input())
(prev, current) = fibonacci(K)
print(current, prev)
