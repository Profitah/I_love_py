def cntGather():
    numList = []
    count = 0

    while count < 10:
        try:
            intN = int(input().strip())
            intRmd = intN % 42
            if intRmd not in numList:
                numList.append(intRmd)
            count += 1
        except ValueError:
            print("정수를 입력해주세요.")

    print(len(numList))

cntGather()
