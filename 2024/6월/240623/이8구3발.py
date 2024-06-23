def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])
    total = 0
    
    for i in range(n):
        a = int(data[i + 1])
        if a == -1:
            total -= 1
        elif a == 1:
            total += 1
    
    if total > 0:
        print("Right")
    elif total < 0:
        print("Left")
    else:
        print("Stay")

if __name__ == "__main__":
    main()
