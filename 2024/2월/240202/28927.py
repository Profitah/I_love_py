maxTimes = list(map(int, input().split()))
melTimes = list(map(int, input().split()))

maxTime = 3 * maxTimes[0] + 20 * maxTimes[1] + 120 * maxTimes[2]
melTime = 3 * melTimes[0] + 20 * melTimes[1] + 120 * melTimes[2]

if maxTime > melTime:
    print("Max")
elif maxTime < melTime:
    print("Mel")
else:
    print("Draw")