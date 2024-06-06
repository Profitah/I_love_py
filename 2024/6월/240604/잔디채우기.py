def read_number():
    numlist= input().strip()
    nums = int(numlist)
    return nums

def result(a, b):
    if a < b:
        print("-1")
    elif a > b:
        print("1")
    else:
        print("0")

def main():
    a = read_number()
    b = read_number()
    result(a, b)

if __name__ == "__main__":
    main()
