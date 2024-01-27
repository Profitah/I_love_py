def fibonacci(sequence):
    if sequence <= 1:
        return sequence
    return fibonacci(sequence-1) + fibonacci(sequence-2)  

number = int(input())
print(fibonacci(number))
