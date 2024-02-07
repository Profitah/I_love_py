while True:
    x, y = map(float, input().split())

    if x == 0 or y == 0:
        print("AXIS", end="")
    elif x > 0 and y > 0:
        print("Q1", end="")
    elif x < 0 and y > 0:
        print("Q2", end="")
    elif x < 0 and y < 0:
        print("Q3", end="")
    else:
        print("Q4", end="")

    if x == 0 and y == 0:
        break
    print()
