x = int(input())

fib = [-1]*(x+1) 

def fibo(n):
    if fib[n]!=-1:
        return fib[n]

    if n<2:
        fib[n] = n
        return fib[n]

    fib[n] = fibo(n-1) + fibo(n-2)
    return fib[n]

    

print(fibo(x))