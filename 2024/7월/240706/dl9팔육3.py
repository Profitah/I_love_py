def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    a = int(data[0])
    b = int(data[1])
    
    if 20 <= a <= 23:
        print(24 - a + b)
    else:
        print(b - a)

if __name__ == "__main__":
    main()