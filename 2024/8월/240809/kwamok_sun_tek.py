import math

def main():
    li = [int(input()) for _ in range(6)]
    li[:4] = sorted(li[:4])
    li[4:] = sorted(li[4:])
    
    total = sum(li[1:4]) + max(li[4], li[5])
    
    print(total)

if __name__ == "__main__":
    main()