if __name__ == "__main__":
    A, B, C = map(int, input().split())
    X1, X2, Y1, Y2 = map(int, input().split())

    yMin = min(-A * X1 - C, -A * X2 - C)
    yMax = max(-A * X1 - C, -A * X2 - C)

    dangerMiny = min(B * Y1, B * Y2)
    dangerMaxy = max(B * Y1, B * Y2)

    if yMin >= dangerMaxy or yMax <= dangerMiny:
        print("Lucky")
    else:
        print("Poor")
